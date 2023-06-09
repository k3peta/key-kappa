# key-kappa
![key-kappa画像](https://github.com/k3peta/key-kappa/blob/main/key-kappa.jpg)

神沼三平太が趣味で作った親指レス30キーの自作キーボードのデータです。

ケースなしPCBにゴム足というチープなやつです。めっちゃ薄い。そして角が痛い。

名称の由来はGherkinをパクった感じだから。要はキュウリをパクるような奴からの連想で河童です。結局完全オリジナルになってしまいましたが。

ぎぎぎ。わしは薄くて軽いGherkin配列のキーボードが欲しかったんじゃ……。

## キーボードの入手方法

KiCadのデータとガーバーファイルのZIPファイルを置いておいたので、何とかしてください。たぶんそのまま業者に発注できます。組み立てるには半田付けのスキルが必要です。

完成させるにはKailhロープロファイルスイッチ（Choc v1またはv2に対応）が30個必要です。キートップも同数必要です。他にはProMicro1個とダイオードが30個、あとは適宜ゴム足が必要になります。個人的には表面実装型のダイオードを裏面に並べる方が表面が綺麗なのでおすすめ。ProMicroを付けるときはピンヘッダでもいけるけど、コンスルー対応なのでお好みで何とかしてください。

## ファームウェア

ファームウェアは現時点でのVIA対応を諦めているので、GUIでのキーの変更とかはしばらく落ち着いてから。従って現状QMK Firmwareでソースからコンパイルしてください。コンパイル済みのhexファイル（kappa_default.hex）も置いておきます。なお書き込みはToolboxでよしなにしてください。


## ビルド方法

- まず適宜ダイオードの足を折り、線の入っている方を四角い穴の方にして足を差し込み、30本ハンダづけします。
- ProMicroを取り付けるために、ピンヘッダを上から基板に差し込んでハンダづけします。ピンヘッダは短い側を基板に差し込むといいでしょう。
- ProMicroを上から被せるようにピンヘッダを通してハンダづけします。
- キースイッチを30個差し込んでハンダづけします。ハンダづけを終えたらキーキャップもつけましょう。
- QMK Toolboxでファームウェア（配布されているkappa.hex）を焼きます。リセットボタンがないのでProMocroの向かって右上のGNDとRSTをショートさせてください。
- 完成！


## デフォルトのキー配列

下の画像はkey-kappaのデフォルトのキーマップ（河童配列）です。左右の薬指の位置にそれぞれレイヤーキーがあります。右側のレイヤーキーを押しながら他のキーを押すと、レイヤー１（キーの左上の記号）が入力されます。左側のレイヤーキーはレイヤー２（キーの右下の記号）が入力できます。いわゆる順手シフトで記号とファンクションキー、逆手シフトで数字とカーソルキーという感じ。

日本語を打つ場合に多用される「」、。ーの五種類の記号については。、右手でレイヤーキーを押しながら左手のホームポジションで打ちます。あとの記号は適当に覚えてください。

あとキー長押しでキー側面のキーが入力できます。

MacユーザなのでKarabiner-Elementsを利用して「左右のコマンドキーを英数キーとかなキーとして使う」ように設定している関係で、左右のレイヤーキーにGUIキーを仕込んであります。要するにレイヤー１キーを長押ししながらレイヤー2キーを押すと「英数」キーが入力され。逆にレイヤー2キーを長押ししながらレイヤー1キーを押すと、「かな」キーが入力されるようにしてあります。

![デフォルトのキーマップ画像](https://github.com/k3peta/key-kappa/blob/main/keyboard-layout.png)

この配列を快適に打ちたかっただけです。

参考までに河童配列を適用したPIPI GHERKINのKMK用設定も置いておきます。


## その他カスタマイズ

### BLE Micro Pro用のJSNファイルの実験の成果とか

試行錯誤の結果を置いときます。実機が次元の彼方に旅立っていったので、誰か実験してみてください。多分いけるんで。
