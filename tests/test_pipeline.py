from ragkit.pipeline import Callback, Module


class TestCallback(Callback):
    async def on_test_enter(self, module, state):
        print("Test Callback Enter")

    async def on_test_exit(self, module, state):
        print("Test Callback Exit")


class TestModule(Module):
    def __init__(
        self,
        modules=None,
        exec_in_parallel=False,
        exec_order="before",
        input_key=None,
        output_key=None,
        callbacks=None,
        shared=None,
        event_name="test",
        description="",
        module_name=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            modules,
            exec_in_parallel,
            exec_order,
            input_key,
            output_key,
            callbacks,
            shared,
            event_name,
            description,
            module_name,
            *args,
            **kwargs,
        )

    async def forward(self, state, **kwargs):
        print("Test Module")


async def test_module():
    module = TestModule(callbacks=[TestCallback()])
    await module({})


if __name__ == "__main__":
    import asyncio

    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())
    asyncio.run(test_module())
