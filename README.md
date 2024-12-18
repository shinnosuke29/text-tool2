# kadai

`kadai` は、2つのテキストファイルを比較して違いを見つけるシンプルなツールです。

## 概要

- このプロジェクトは、2つのテキストファイルの違いを比較し、ファイル間の差異を行単位で明確に表示することを目的としています。
- ファイル比較は、文章やコードの変更点を確認したいときに役立ちます。
- 主な機能は、2つのファイルを行ごとに比較し、違いを検出してその内容を表示します。

## インストール方法

以下の手順でプロジェクトをローカル環境にインストールしてください。

## リポジトリをクローン
```git clone https://github.com/ユーザー名/kadai.git```

## ディレクトリに移動
```cd kadai```

## 依存関係をインストール
```pip install -r requirements.txt```

## 使用方法

1. 比較したいテキストファイルを準備します。例えば、`file1.txt` と `file2.txt` を用意します。

2. 以下のコマンドを実行して、2つのファイルの違いを比較します：

    ```bash
    python3 text_compare.py file1.txt file2.txt
    ```

    このコマンドを実行すると、`file1.txt` と `file2.txt` の違いが検出され、結果がコンソールに表示されます。

## 出力例
以下は、file1.txt と file2.txt に違いがあった場合の出力例です：

 ```Differences found: 
    Line 2:
    File1: This is the second line.
    File2: This is the modified second line.
 ```

## ファイル構成
プロジェクト内の主要ファイルは以下の通りです：

- `text_compare.py`
ファイル比較のメインスクリプト。

主な機能：

 - 2つのテキストファイルを読み込み、行単位で比較します。

 - 一致しない行がある場合、その内容と行番号を表示します。

 - ファイルが一致している場合は「Files are identical」と出力します。

- `file1.txt`
比較に使用するサンプルテキストファイル。

- `file2.txt`
比較に使用するサンプルテキストファイル。

- `README.md`
このプロジェクトの概要や使用方法を説明するファイル。

- `.gitignore`
Git 管理から除外するファイルやディレクトリを指定したファイル。

## 貢献方法
このリポジトリをフォークする。

新しいブランチを作成する。（例：`git checkout -b feature/YourFeature`）

コードを変更し、コミットする。（`git commit -m 'Add some feature'`）

変更をプッシュする。（`git push origin feature/YourFeature`）

プルリクエストを作成する。

## クレジット
このプロジェクトは個人的な目的で作成され、以下のライブラリに依存しています：

- Python 3.x
