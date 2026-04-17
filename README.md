# STS2攻略アドバイザー（実験）

ローカルLLM（ollama + OpenWebUI）とRAGを使って、Slay the Spire 2の攻略アドバイザーを構築するプロジェクトです。

## 環境

- ollama 0.20.7
- OpenWebUI v0.8.10
- モデル：gemma4:26b
- Python 3.10.6

## 構成

- `scrape.py` - mobalytics.ggからSTS2攻略情報を取得するスクリプト（Selenium使用）
- `config.json` - スクレイピング対象URLの管理ファイル

## 関連記事

- [第1記事：環境構築編](https://zenn.dev/minagi_llm/articles/98bb57a9dfa689)
- [第2記事：RAG構築編](https://zenn.dev/minagi_llm/articles/b9f37e919e7d34)
- 第3記事：スクレイピング改善・RAGの限界編（公開予定）

## 使い方

1. 仮想環境を作成して有効化
2. `pip install requests beautifulsoup4 selenium webdriver-manager`
3. `config.json` にスクレイピング対象URLを記載
4. `python scrape.py` を実行
5. 取得したtxtをOpenWebUIのナレッジベースに登録

## 注意事項

スクレイピング実行前に、対象サイトの `robots.txt` と利用規約を必ず確認してください。
