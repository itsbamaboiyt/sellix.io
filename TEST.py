from sellix.abc.modals import Shop
import msgspec
import pathlib


class Sh(msgspec.Struct):
    data: Shop


with pathlib.Path("example/self.json").open("r") as f:
    strs = f.read()
    base = msgspec.json.decode(strs, type=Sh, strict=False)
    shop = base.data
