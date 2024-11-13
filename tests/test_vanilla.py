from ragkit.pipeline import PerfTracker
from ragkit.pipeline.vanilla import build_vanilla_pipeline


async def test_vanilla():
    pipeline = build_vanilla_pipeline(
        llm_model="glm-4-flash", callbacks=[PerfTracker(print_enter=True)]
    )
    # res = await pipeline({"query": "What is the capital of France?"})
    # print(res)
    async for t in pipeline.stream({"query": "What is the capital of France?"}):
        print(t)


if __name__ == "__main__":
    import asyncio

    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())
    asyncio.run(test_vanilla())
