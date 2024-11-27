# kadai

## 概要
`kadai` は、2つのテキストファイルを比較して違いを見つけるためのシンプルなツールです。このツールは主に、文章やデータの比較を行う際に使用できます。

## 特徴
- テキストファイルの行単位での違いを検出
- ファイル間で一致しない行を詳細に表示
- Python でシンプルに実装されており、手軽に使用可能

## 必要要件
- Python 3.x

## 使用方法
1. このリポジトリをクローンします：
    ```bash
    git clone https://github.com/ユーザー名/kadai.git
    cd kadai
    ```
2. 比較したいテキストファイルを準備します。
    - 例: `file1.txt` と `file2.txt`
3. 以下のコマンドを実行して比較を行います：
    ```bash
    python3 text_compare.py file1.txt file2.txt
    ```

## 出力例
以下は、`file1.txt` と `file2.txt` に違いがあった場合の出力例です：

```plaintext
Differences found: 
Line 2:
  File1: This is a line in file1.
  File2: This is a modified line in file2.

## ファイル構成
プロジェクト内の主要ファイルは以下の通りです：

- `text_compare.py`  
  ファイル比較のメインスクリプト。  
  **主な機能**：
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

## ライセンス
このプロジェクトはMITライセンスのもとで公開されています。詳細は `LICENSE` ファイルをご確認ください。

