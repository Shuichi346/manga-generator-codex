<table>
  <thead>
    <tr>
      <th style="text-align:center"><a href="README_ja.md">日本語</a></th>
      <th style="text-align:center"><a href="README.md">English</a></th>
    </tr>
  </thead>
</table>

# Codex 用マンガ制作プラグイン

Manga Production は、ストーリー草稿・キャラクター資料・スタイルノートからマンガページの企画・生成を行うための Codex プラグインです。`manga-generation` スキルを提供しており、草稿をページごとのビート（場面展開）に展開し、同梱のマンガページテンプレートを選択し、コマごとの描画指示を作成し、`$imagegen` を使って各完成マンガページをコマ画像に分割せず1ページ全体として生成します。

## 機能

- 草稿・脚本・ストーリーコンセプトからマンガページを企画します。
- 3 つの展開モードをサポートしています：`Original`（原文）・`Slight Expansion`（軽度展開）・`Expansion`（展開）。
- 同梱のブランク原稿ベースおよびナンバリングされたマンガコマレイアウトから選択します。
- テンプレート選択・ページ目的・継続性ノート・描画指示・セリフ・効果音・フキダシ配置を含むページプランを生成します。
- パネル枠・コマの余白を保持した白黒マンガページ全体を生成するよう `$imagegen` を誘導します。
- 生成されたマンガページは `output/manga-pages/` に保存され、Git の管理対象外となります。

## テンプレートプレビュー

このプラグインには、再利用可能なマンガページテンプレートが `plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/` に同梱されています。

<img src="plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/generated-layout-5-panel-balanced.png" alt="5コママンガページテンプレート" width="480">

## 要件

- プラグインサポートを備えた Codex。
- 最終マンガページ画像を生成する際に `$imagegen` が利用可能であること。
- `generate_manga_templates.py` でテンプレート PNG を再生成する場合のみ、Pillow を含む Python 3 が必要です。

このリポジトリでは API キー・認証情報・環境変数は定義されていません。

## インストール

```text
@plugin-creator  Please install the `manga-generator-codex/plugins/manga-production` plugin.
If there is no location to install the local Codex plugin, create one.
```

もしくは、

このプラグインを Codex に追加する際は、プラグインのルートディレクトリを使用してください：

```text
plugins/manga-production
```

マニフェストの場所：

```text
plugins/manga-production/.codex-plugin/plugin.json
```

## 使い方

ストーリー草稿および関連する参考画像を用意して、Codex からスキルを呼び出してください：

```text
Use $manga-generation to make a 5-page manga from my draft and references.
```

展開モードを指定することもできます：

```text
Use $manga-generation in Slight Expansion mode for this story draft.
```

デフォルトでは、スキルは以下の設定を使用します：

- 展開モード：`Original`
- 最大ページ数／画像数：`5`
- テンプレートフォルダ：スキルディレクトリからの相対パス `assets/Manga_Panel_Layout_Template/`
- 出力フォルダ：リポジトリルートからの相対パス `output/manga-pages/`

スキルは生成前に各ページを企画します。各 `$imagegen` リクエストは、すべてのコマ・枠線・フキダシ・セリフ・効果音・ページ構成を含む完全なマンガページを1枚生成する必要があります。

## 開発

以下のコマンドで、決定論的なブランク原稿ベース・生成済みパネルテンプレート・`template_manifest.json` を再生成できます：

```bash
python3 plugins/manga-production/scripts/generate_manga_templates.py
```

スクリプトの出力先：

```text
plugins/manga-production/skills/manga-generation/assets/Manga_Panel_Layout_Template/
```

GitHub から公開できる状態を維持するため、プラグインは `plugins/manga-production/` 内で自己完結するようにしてください。

## プロジェクト構成

```text
.
├── plugins/manga-production/
│   ├── .codex-plugin/plugin.json
│   ├── assets/manga-production-icon.svg
│   ├── scripts/generate_manga_templates.py
│   └── skills/manga-generation/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/Manga_Panel_Layout_Template/
│       └── references/
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE
├── NOTES.md
└── README.md
```

## プライバシー

このプラグインは認証情報を保存せず、外部サービスとの連携も定義していません。マンガ草稿・参考画像・生成されたページプラン・出力画像は、ユーザーが明示的に共有しない限り、アクティブな Codex ワークスペース内に保持されます。

## ライセンス

このリポジトリは MIT ライセンスの下で公開されています。[LICENSE](LICENSE) を参照してください。