# 第14章ドリル：init.lua を最初に変えるべき設定

← [目次へ戻る](../index.md)　｜　参照: [`nvim_engineer_reference.md` §14](../nvim_engineer_reference.md)

---

## 準備

`init.lua` を開いてください：

```
nvim ~/.config/nvim/init.lua
```

---

## 練習問題

### Q1. `relativenumber` を有効にする（最重要）

1. `init.lua` を開いてください
2. `/relativenumber` で現在の設定を検索してください
3. すでに設定されている場合は `true` になっているか確認してください
4. 設定がない場合は `vim.opt.number = true` の行を探して、その下に以下を追加してください：

```lua
vim.opt.relativenumber = true
```

5. `:w` で保存し、`:source %` でリロードしてください（または Neovim を再起動）
6. 行番号が相対表示になったことを確認してください

> **効果**: `5dd` や `3j` などの数値 + コマンドが直感的に使えるようになります。カーソル行が `0`、上下に 1, 2, 3... と表示されます。

---

### Q2. `scrolloff` を設定する

1. `/scrolloff` で既存の設定を確認してください
2. 設定がない場合は以下を追加してください：

```lua
vim.opt.scrolloff = 8
```

3. `:source %` でリロードしてください
4. ファイルの中ほどで `Ctrl-d` を連打してください
5. カーソルが常に画面上下から8行の余白を保って移動することを確認してください

---

### Q3. `wrap` をオフにする

1. 以下を設定に追加してください：

```lua
vim.opt.wrap = false
```

2. `:source %` でリロードしてください
3. 長い1行のコードを含むファイルを開いて、折り返されなくなったことを確認してください

---

### Q4. `undofile` を有効にする

1. 以下を設定に追加してください：

```lua
vim.opt.undofile = true
```

2. `:source %` でリロードしてください
3. ファイルを編集して `:wq` で保存・終了してください
4. 再び同じファイルを開き、`u` を押してください
5. Neovim を終了する前の変更もアンドゥできることを確認してください

> **効果**: Neovim を閉じてもアンドゥ履歴が永続化されます。誤った変更を後から取り消せます。

---

### Q5. `colorcolumn` を設定する

1. 以下を設定に追加してください：

```lua
vim.opt.colorcolumn = '100'
```

2. `:source %` でリロードしてください
3. 100文字を超える長い行を含むファイルを開いてください
4. 100列目にガイド線が表示されることを確認してください

---

### Q6. `tabstop` / `shiftwidth` を設定する

プロジェクトに合わせてタブ幅を変更します（Python は 4、JavaScript/TypeScript は 2 が一般的）：

1. 現在の設定を確認してください：`:set tabstop?` / `:set shiftwidth?`
2. 必要に応じて以下を設定に追加してください：

```lua
vim.opt.tabstop = 4      -- Python の場合
vim.opt.shiftwidth = 4
```

3. `>>` で行をインデントして、幅が変わったことを確認してください

---

### Q7. 設定を確認する

1. `:set relativenumber?` を実行して設定値を確認してください
2. `:set scrolloff?` も確認してください
3. 設定が効いていない場合は、`init.lua` の構文エラーを `:checkhealth` で確認してください

---

### Q8. 総合チャレンジ

1. `~/.config/nvim/init.lua` を開いて、Q1〜Q6 の設定がすべて入っているか確認してください
2. 足りない設定を追加してください
3. `:source %` でリロードして動作を確認してください
4. `relativenumber` + `scrolloff = 8` の状態で、このドリルの任意の章に戻って操作を試してみてください。特に `5j` `10k` などの数値 + モーションが使いやすくなっていることを実感してください

---

## 設定の完成形（参考）

```lua
-- ~/.config/nvim/init.lua の options セクションに追加
vim.opt.relativenumber = true  -- 相対行番号
vim.opt.scrolloff = 8          -- 上下8行の余白
vim.opt.wrap = false           -- 長い行を折り返さない
vim.opt.tabstop = 4            -- タブ幅（Python は 4）
vim.opt.shiftwidth = 4
vim.opt.colorcolumn = '100'    -- 100桁ガイド線
vim.opt.undofile = true        -- アンドゥ履歴を永続化
```

> **最後に**: 設定は少しずつ変えること。一度に大量に変えると何が原因でおかしくなったかわからなくなります。変更したら必ず動作確認してから次へ進んでください。
