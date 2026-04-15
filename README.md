# STS2攻略アドバイザー

ローカルLLM（ollama + OpenWebUI）とRAGを使って、Slay the Spire 2の攻略アドバイザーを構築するプロジェクトです。

## 環境

- ollama 0.20.7
- OpenWebUI v0.8.10
- モデル：gemma4:e4b
- Python 3.10.6

## 構成

- `scrape.py` - wiki.ggからSTS2情報を取得するスクリプト（403対策で手動コピーに切り替え）

## 関連記事

- [第1記事：環境構築編](https://zenn.dev/minagi_llm/articles/98bb57a9dfa689)
- 第2記事：RAG構築編（公開予定）

## 使い方

1. 仮想環境を作成して有効化
2. `pip install requests beautifulsoup4`
3. `python scrape.py` を実行
4. `sts2_wiki_docs/` に取得したtxtをOpenWebUIのナレッジベースに登録