# kadai

`kadai` は、2つのテキストファイルを比較して違いを見つけるシンプルなツールです。

## 概要

- このプロジェクトは、2つのテキストファイルの違いを比較し、ファイル間の差異を行単位で明確に表示することを目的としています。
- ファイル比較は、文章やコードの変更点を確認したいときに役立ちます。
- 主な機能は、2つのファイルを行ごとに比較し、違いを検出してその内容を表示します。

## インストール方法

以下の手順でプロジェクトをローカル環境にインストールしてください。

```bash
# リポジトリをクローン
git clone https://github.com/ユーザー名/kadai.git

# ディレクトリに移動
cd kadai

# 依存関係をインストール
pip install -r requirements.txt

## 使用方法

1. 比較したいテキストファイルを準備します。例えば、`file1.txt` と `file2.txt` を用意します。

2. 以下のコマンドを実行して、2つのファイルの違いを比較します：

    ```bash
    python3 text_compare.py file1.txt file2.txt
    ```

   このコマンドを実行すると、`file1.txt` と `file2.txt` の違いが検出され、結果がコンソールに表示されます。

## 出力例

以下は、`file1.txt` と `file2.txt` に違いがあった場合の出力例です：

```plaintext
Differences found: 
Line 2:
  File1: This is the second line.
  File2: This is the modified second line.
