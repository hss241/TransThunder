# This software translates chats in battle with WarThunder  
## How to use ( English )  
1. Start
2. Write the target language in lang of transthunder.ini generated in the same directory ( if you want to translate other languages into Japanese, change en to ja )
3. Restart after changing the target language
4. Chats in battle are translated and appear on the console!

## Display translation results in a browser ( Possible with smartphone )
1. Rewrite from False to True in browse of transthunder.ini
2. Write port number in flask and websocket of transthunder.ini ( Usually there is no problem even if it is not rewritten )
3. Write IP address in host of transthunder.ini ( Allow access only to this IP address )
4. Enter the address and port number of the computer that launched this software into the browser
    Example ) http://localhost:10101/
5. Displayed the same as the console!

### Translated
- Other languages

### Not translated
- Target language

---
# WarThunderでの戦闘中のチャットを翻訳するソフトです  
## 使い方(日本語)
1. 起動する
2. 同階層に生成されるtransthunder.iniのlangに翻訳先の言語を書く(他言語を日本語に翻訳するならenをjaに変える)
3. 翻訳先言語を変更したら、再起動する
4. 戦闘中のチャットが翻訳されてコンソールに出てくる！

## 翻訳結果をブラウザで表示できます(スマホでも可能)
1. transthunder.iniのbrowseのFalseをTrueに書き換える
2. transthunder.iniのflaskとwebsocketにポート番号を書く(大抵書き換えなくても問題はない)
3. transthunder.iniのhostにIPアドレスを書く(このIPアドレスに対するアクセスだけ許可)
4. このソフトを起動したPCのIPアドレスとポート番号をブラウザに入力
    例)http://localhost:10101/
5. コンソールと同じように表示される！

### 翻訳されるもの
- 他の言語

### 翻訳されないもの
- 翻訳先と同じ言語

---
Icon
 - http://icooon-mono.com/10735-%e3%82%bc%e3%83%ad%e6%88%a6%e3%81%ae%e3%82%a2%e3%82%a4%e3%82%b3%e3%83%b3/

Import
- **py-googletrans** by **SuHun Han**
  - https://github.com/ssut/py-googletrans

- **colorama** by **Jonathan Hartley**
  - https://github.com/tartley/colorama

- **python-websocket-server** by **Pithikos**
  - https://github.com/Pithikos/python-websocket-server

- **flask** by **pallets**
  - https://github.com/pallets/flask

- **flask-cors** by **corydolphin**
  - https://github.com/corydolphin/flask-cors
