from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ローカル上でフロントからフェッチする場合、CORSの設定が必要
# TODO：APIをサーバーに乗せた際に、必要なければ削除する
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    response = {
        "status": "success",
        "totalResults": 6,
        "results":
            [
                {
                    "article_id": "9834f9190fad7132",
                    "title": (
                        "「SoftBankウインターカップ2024」男子・九州学院(熊本)2回戦へ(KAB熊本朝日放送)"
                        ),
                    "link": (
                        "https://news.yahoo.co.jp/articles/"
                        "60d07f8f3c32349dfec9216394cad299544b1c9a?source=rss"
                        ),
                    "image_url": (
                        "https://newsatcl-pctr.c.yimg.jp"
                        "/t/amd-img/20241224-00010000-kab-000-1-view.jpg?"
                        "exp=10800&h=253&pri=l&w=450"
                        ),
                    "category": ["domestic"]
                },
                {
                    "article_id": "9834f9190fad7132",
                    "title": (
                        "吉田沙保里、スカイツリーのさきっぽへし折る"
                    ),
                    "link": (
                        "https://news.yahoo.co.jp/articles/"
                        "60d07f8f3c32349dfec9216394cad299544b1c9a?source=rss"
                    ),
                    "image_url": (
                        "https://image.lgtmoon.dev/317256"
                    ),
                    "category": ["domestic"]
                },
                {
                    "article_id": "00001",
                    "title": (
                        "「タイムカプセルを探していただけなんです」"
                        "学校の地面からウラン湧き出る、生徒が泥酔状態に"
                    ),
                    "link": (
                        "https://news.yahoo.co.jp/articles/"
                        "60d07f8f3c32349dfec9216394cad299544b1c9a?source=rss"
                    ),
                    "image_url": (
                        "https://newsatcl-pctr.c.yimg.jp/t/amd-img/"
                        "20241224-00010000-kab-000-1-view.jpg"
                        "?exp=10800&h=253&pri=l&w=450"
                    ),
                    "category": ["domestic"]
                },
                {
                    "article_id": "00002",
                    "title": (
                        "真木よう子大量発生 - ティンコンカンコン警備隊発足"
                    ),
                    "link": (
                        "https://news.yahoo.co.jp/articles/"
                        "60d07f8f3c32349dfec9216394cad299544b1c9a?source=rss"
                    ),
                    "image_url": (
                        "https://newsatcl-pctr.c.yimg.jp/t/amd-img/"
                        "20241224-00010000-kab-000-1-view.jpg?"
                        "exp=10800&h=253&pri=l&w=450"
                    ),
                    "category": ["domestic"]
                },
                {
                    "article_id": "00003",
                    "title": (
                        "K-POPアイドル、軽POPアイドルに"
                    ),
                    "link": (
                        "https://news.yahoo.co.jp/articles/"
                        "60d07f8f3c32349dfec9216394cad299544b1c9a?source=rss"
                    ),
                    "image_url": (
                        "https://newsatcl-pctr.c.yimg.jp/t/amd-img/"
                        "20241224-00010000-kab-000-1-view.jpg?"
                        "exp=10800&h=253&pri=l&w=450"
                    ),
                    "category": ["domestic"]
                },
                {
                    "article_id": "00004",
                    "title": (
                        "「こんなはずじゃなかった」あばれる君破産"
                    ),
                    "link": (
                        "https://news.yahoo.co.jp/articles/"
                        "60d07f8f3c32349dfec9216394cad299544b1c9a?source=rss"
                    ),
                    "image_url": (
                        "https://newsatcl-pctr.c.yimg.jp/t/amd-img/"
                        "20241224-00010000-kab-000-1-view.jpg?"
                        "exp=10800&h=253&pri=l&w=450"
                    ),
                    "category": ["domestic"]
                }
            ]
    }
    return response
