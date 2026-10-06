# swo2026-online-secretariat / source ブランチ

公開中の main（Vercel）とは別に、LPの組み立て元を保管するブランチ。

- src/template.html … ver1.10（10/5修正反映）の元テンプレート。画像は {{IMG:名前}} で参照
- src/imgs.json … 画像（base64）。build.py が template に埋め込んで index.html を作る
- src/build.py … `python3 build.py` で index.html を生成（BUILD_TAG・FAQ文言もここ）
- src/template_v1.10_hero_candidate.html … アイキャッチ縮小案（保留中）
- delivered_index_261006.html … 10/6 に永田様へ納品した index.html（GAタグ G-75V5K5C3SR 入り）
- qa/ … 横スクロール・折り返し・ボタンはみ出し・スクリーンショット用のPlaywrightスクリプト

WordPress組み込み時は src/template.html の構成と CSS を土台にする。
