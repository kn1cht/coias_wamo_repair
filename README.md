# COIAS WAMO REPAIR

[COIAS](https://web-coias.u-aizu.ac.jp/)で2023年11月～12月に行われたデータ修正を手元のsend_mpc.txtに適用します

- 多数のファイルがあっても全自動で変換します
- ディレクトリを分けている場合も、その構造を保ったまま変換します
- もともとのデータは書き換えず、新しいディレクトリに書き込みます
    - 旧ディレクトリ名、新ディレクトリ名は指定できます
- 変換に成功した行数や失敗した行についての詳細を出力します

## 注意
- 非公式なスクリプトです。**動作を理解したうえで、自己責任で実行してください**
- 元のファイルの上書きは原則行わない仕様ですが、**必ずバックアップを取ってから実行してください**
- send_mpc.txt以外は変換しません。final_all.txtなどはご自身で新しいディレクトリにコピーしてください

## Environment

- Python 3.x

## Usage
### wamo_repair.py

```bash
python wamo_repair.py
```

旧ディレクトリ名、新ディレクトリを聞かれるので入力してください（カレントディレクトリにディレクトリを作ってまとめておくのが楽です）。

旧ディレクトリ名は入力必須です。
新ディレクトリ名はオプションです。入力されなかった場合は、`new_{旧ディレクトリ名}`とします。

### wamo_repair.ipynb
Python Notebook版です。動作は同じです。

## LICENSE
MIT
