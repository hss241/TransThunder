# This software translates chats in battle in WarThunder  
## How to use ( English )  
1. Start TransThunder.exe
2. Write the target language in the transthunder.ini's lang, which is generated in the same directory ( If you want to translate other languages to Japanese, change en to ja )
3. Restart after changing the target language
4. The chat in combat is translated and comes out on the console!

## Beep when you receive a chat with or without a translation
1. Rewrite transthunder.ini's beep to True

## You can view the translation results in your browser ( Even on your smartphone )
1. Rewrite transthunder.ini's browse to True
2. Write the port number in the transthunder.ini's flask and websocket ( Usually no problem without rewriting )
3. Write an IP address in the transthunder.ini's host ( Only access to this IP address is allowed )
4. Enter the IP address and port number of the PC on which this software is running into your browser
    Example ) http://localhost:10101/
5. It shows up just like the console!

## More accurate translation
- Setting accuracy to True in transthunder.ini will result in a more accurate translation
  - You need to install Firefox (79.0) or Chrome (84.0.4147.30) or above version
    - Firefox takes precedence
      - Unsupported languages will still be translated as before

### Translated
- Other languages

### Not translated
- Target language

---
# WarThunderでの戦闘中のチャットを翻訳するソフトです  
## 使い方(日本語)
1. TransThunder.exeを起動する
2. 同階層に生成されるtransthunder.iniのlangに、翻訳先の言語を書く(他言語を日本語に翻訳するならenをjaに変える)
3. 翻訳先言語を変更したら、再起動する
4. 戦闘中のチャットが翻訳されてコンソールに出てくる！

## 翻訳の有無にかかわらず、チャットを受信した時にビープ音を鳴らす
1. transthunder.iniのbeepをTrueに書き換える

## 翻訳結果をブラウザで表示できます(スマホでも可能)
1. transthunder.iniのbrowseをTrueに書き換える
2. transthunder.iniのflaskとwebsocketにポート番号を書く(大抵書き換えなくても問題はない)
3. transthunder.iniのhostにIPアドレスを書く(このIPアドレスに対するアクセスだけ許可)
4. このソフトを起動しているPCのIPアドレスとポート番号をブラウザに入力
    例)http://localhost:10101/
5. コンソールと同じように表示される！

## さらに正確な翻訳を行う
- transthunder.iniでaccuracyをTrueに設定すると、より正確な翻訳になります
  - Firefox(79.0)またはChrome(84.0.4147.30)以上のバージョンをインストールする必要があります
    - Firefoxが優先されます
      - サポートされていない言語は以前と同じように翻訳されます

### 翻訳されるもの
- 他の言語

### 翻訳されないもの
- 翻訳先と同じ言語

---
### Icon
- https://icooon-mono.com/
  - Search by **Zero fighter**

### Import
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

- **win_unicode_console** by **Drekin**
  - https://github.com/Drekin/win-unicode-console

- **selenium** by **Selenium**
  - https://github.com/SeleniumHQ/selenium


## Notice
- This software includes the work that is distributed in the Apache License 2.0