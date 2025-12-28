import shlex
import subprocess
import threading
import sys
from typing import List, Optional, Tuple, Union, Dict


def run_shell(
    cmd: Union[str, List[str]],
    cwd: Optional[str] = None,
    env: Optional[Dict[str, str]] = None,
    timeout: Optional[float] = None,
    check: bool = False,
    capture_output: bool = True,
    text: bool = True,
    shell: bool = False,
    stream: bool = False,
    encoding: Optional[str] = None,
) -> Tuple[int, str, str]:
    """
    运行一个 shell 命令并返回 (returncode, stdout, stderr)。

    参数:
    - cmd: 命令字符串或列表
    - cwd: 工作目录
    - env: 额外环境变量（替代或扩展父进程环境）
    - timeout: 超时时间（秒）
    - check: 如果为 True 且返回码非 0 则抛出 CalledProcessError
    - capture_output: 为 False 时不捕获输出（仅在 stream=False 时有效）
    - text: 是否以文本模式处理输出（True -> str）
    - shell: 是否通过 shell 运行（命令为字符串时可用）
    - stream: 实时打印 stdout/stderr 并同时捕获（适合长时间运行的命令）

    返回:
    - (returncode, stdout, stderr)
    """
    if stream:
        # 使用 Popen + 线程流式读取 stdout/stderr，同时收集输出
        if isinstance(cmd, str) and not shell:
            args = shlex.split(cmd)
        else:
            args = cmd

        proc = subprocess.Popen(
            args,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=text,
            shell=shell,
            bufsize=1,
            encoding="utf-8" if encoding else None,
        )

        stdout_parts: List[str] = []
        stderr_parts: List[str] = []

        def _reader(pipe, store, out_stream):
            try:
                for line in iter(pipe.readline, ""):
                    store.append(line)
                    out_stream.write(line)
                    out_stream.flush()
            finally:
                pipe.close()

        threads = []
        if proc.stdout:
            t = threading.Thread(
                target=_reader,
                args=(proc.stdout, stdout_parts, sys.stdout),
                daemon=True,
            )
            t.start()
            threads.append(t)
        if proc.stderr:
            t2 = threading.Thread(
                target=_reader,
                args=(proc.stderr, stderr_parts, sys.stderr),
                daemon=True,
            )
            t2.start()
            threads.append(t2)

        try:
            returncode = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            returncode = proc.wait()

        for t in threads:
            t.join()

        stdout = "".join(stdout_parts) if text else b"".join(stdout_parts)  # type: ignore
        stderr = "".join(stderr_parts) if text else b"".join(stderr_parts)  # type: ignore

        if check and returncode != 0:
            raise subprocess.CalledProcessError(
                returncode, cmd, output=stdout, stderr=stderr
            )

        return returncode, stdout, stderr

    else:
        # 简单使用 subprocess.run
        if isinstance(cmd, str) and not shell:
            args = shlex.split(cmd)
        else:
            args = cmd

        completed = subprocess.run(
            args,
            cwd=cwd,
            env=env,
            capture_output=capture_output,
            text=text,
            shell=shell,
            timeout=timeout,
        )

        if check and completed.returncode != 0:
            raise subprocess.CalledProcessError(
                completed.returncode,
                cmd,
                output=completed.stdout,
                stderr=completed.stderr,
            )

        stdout = completed.stdout if capture_output else ""
        stderr = completed.stderr if capture_output else ""
        return completed.returncode, stdout, stderr
