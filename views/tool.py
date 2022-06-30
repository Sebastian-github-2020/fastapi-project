from fastapi import APIRouter
import os

"""
工具类
"""
tool_router = APIRouter()


def cmd_runner(command: str):
    d = os.popen(cmd=command)
    f = d.read()
    return f


@tool_router.get("/dns")
def tool_flush_dns():
    return {
        "msg": cmd_runner("ipconfig/flushdns")
    }
