from typing import Optional

from polars import LazyFrame
from weavehr.callbacks.proto import AstValue, CallbackProtocol, CallbackResult, to_expr
from weavehr.callbacks.registry import register_callback_cls


@register_callback_cls
class NoOp(CallbackProtocol):
    def __init__(
        self,
        col: AstValue,
        output: Optional[str] = None,
    ) -> None:
        self.col = col
        self.output = output

    def __call__(self, lf: LazyFrame) -> CallbackResult:
        expr = to_expr(lf, self.col)
        if self.output is None:
            return expr
        return expr.alias(self.output)
