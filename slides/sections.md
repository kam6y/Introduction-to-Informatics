<!-- .slide: class="layout-section" -->
## Intro / Goals
<p class="subtitle">到達点・評価軸・90枚のロードマップ</p>

---

<!-- .slide: class="layout-section" -->
## Foundations
<p class="subtitle">要件定義・設計・テストの種類</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Foundationsの学習目標</h2>
  <ul>
    <li>Vモデルで開発工程の全体像を説明できる</li>
    <li>品質・納期・コストのトレードオフを意識する</li>
    <li>要件→設計→テストの対応関係を説明できる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-full-bleed dev-flow-slide" data-background-color="#f4f5f7" -->
<div class="overlay overlay-solid">
  <h2>開発の流れ（Vモデル）</h2>
  <p class="subtle">定義・設計とテストの対応関係</p>
  <ul class="subtle">
    <li><strong>要件定義</strong> : 2割、<strong>開発（設計＋実装）</strong> : 6.5割、<strong>テスト</strong> : 1.5割  ←割合はIPAより</li>
  </ul>
</div>
<img class="dev-flow-image" src="assets/dev-flow.svg" alt="開発の流れ（Vモデル）の全体像" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>要件定義で合意を作る</h2>
  <ul>
    <li>目的とスコープ（作る/作らない）</li>
    <li>成果物・評価基準（受入条件）</li>
    <li>ステークホルダーと決裁者を明確化</li>
  </ul>
</div>
<div class="callout">
  <p><strong>成果物例</strong></p>
  <ul>
    <li>目的・課題の整理</li>
    <li>主要ユースケース</li>
    <li>制約・前提条件</li>
    <li>機能要件・非機能要件</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>機能要件をユーザー行動で書く</h2>
  <ul>
    <li>ユースケース/ユーザーストーリーで整理</li>
    <li>入力・出力・例外を明確化</li>
    <li>受入条件をテスト可能にする</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>「利用者は予約を変更できる」</p>
  <p class="subtle">期限・通知・制約を追記</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>非機能要件は数値で固定する</h2>
  <ul>
    <li>性能: 応答時間・同時接続</li>
    <li>可用性: 可用性SLO(稼働率) / RTO(目標復旧時間) / RPO(目標復旧時点)</li>
    <li>セキュリティ・法規制・運用要件</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>主要画面の応答目標: 3秒</p>
  <p>SLO: 99.9%</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>粒度を合わせて手戻りを減らす</h2>
  <ul>
    <li>MVPとフェーズ分割で優先度を決める</li>
    <li>ワイヤー/プロトタイプで認識合わせ</li>
    <li>変更は影響範囲とコストを可視化</li>
  </ul>
</div>
<div class="callout">
  <p><strong>合意の道具</strong></p>
  <ul>
    <li>ワイヤーフレーム</li>
    <li>プロトタイプ</li>
    <li>優先度表</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>外部設計と内部設計を分ける</h2>
  <ul>
    <li>外部設計: 画面 / API / 入出力</li>
    <li>内部設計: データ / ロジック / 構成</li>
    <li>要件↔設計のトレーサビリティを維持</li>
  </ul>
</div>
<div class="callout">
  <p><strong>成果物例</strong></p>
  <ul>
    <li>画面遷移図・API仕様</li>
    <li>ER図・シーケンス図</li>
    <li>構成図・運用設計</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-3col corner-image" -->
<h2>設計の意思決定を残す</h2>
<div>
  <h3>構成</h3>
  <ul>
    <li>モノリス: 速く作れるが、変更影響が大きい</li>
    <li>マイクロサービス: 独立性が高いが、運用コスト増</li>
  </ul>
</div>
<div>
  <h3>Build vs Buy</h3>
  <ul>
    <li>自社開発: 柔軟に改善できるが、時間/保守負担</li>
    <li>SaaS: 立ち上げが速いが制約/コストがかかる</li>
  </ul>
</div>
<div>
  <h3>品質軸</h3>
  <ul>
    <li>性能重視? コスト重視?</li>
    <li>非機能がどれだけ重視されるかによる</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>テストの種類と対応関係</h2>
  <ul>
    <li>単体テスト: 関数/モジュール</li>
    <li>結合テスト: 境界/連携</li>
    <li>システムテスト: 外部仕様</li>
    <li>受入テスト: 要件/受入条件</li>
  </ul>
</div>
<div class="callout">
  <p><strong>対応関係</strong></p>
  <ul>
    <li>要件 → 受入テスト</li>
    <li>外部設計 → システムテスト</li>
    <li>内部設計 → 結合テスト</li>
    <li>実装 → 単体テスト</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>テスト計画は観点から作る</h2>
  <ul>
    <li>正常/異常/境界の観点で網羅</li>
    <li>テストデータと環境を先に準備</li>
    <li>自動化は「変更頻度×影響度」から</li>
  </ul>
</div>
<div class="callout">
  <p><strong>テスト実装の優先度の式</strong></p>
  <p class="subtle">変更頻度 × 影響度</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>ミニケース：予約アプリ</h2>
  <ul>
    <li>要件: 変更/キャンセル/通知/在庫反映</li>
    <li>設計: 予約API + 通知キュー + 在庫ロック</li>
    <li>テスト: 期限/通知遅延/二重予約/同時操作</li>
  </ul>
</div>
<div class="callout">
  <p><strong>受入条件（例）</strong></p>
  <ul>
    <li>変更は前日23:59まで</li>
    <li>キャンセル後は在庫が即時復活</li>
  </ul>
  <p class="subtle">通知は30秒以内に送信</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Foundations自己チェック</h2>
  <ul>
    <li>Vモデルの対応関係を図で説明できる</li>
    <li>要件定義の成果物を3つ言える</li>
    <li>非機能要件を数値で書ける（SLO/RTO/RPO）</li>
    <li>テスト観点（正常/異常/境界）を挙げられる</li>
    <li>ミニケースの受入条件を2つ作れる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Git / GitHubに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Git / GitHub
<p class="subtitle">ブランチ/PR/レビューと履歴の読み方</p>

---

<!-- .slide: class="layout-section" -->
## Testing & Observability
<p class="subtitle">unit/integration/e2e・ログ/メトリクス/トレース</p>

---

<!-- .slide: class="layout-section" -->
## Docker
<p class="subtitle">イメージ/コンテナ/レジストリと基本コマンド</p>

---

<!-- .slide: class="layout-section" -->
## Web Apps & Cloud
<p class="subtitle">HTTP/API・3層構成・クラウド責務分界</p>

---

<!-- .slide: class="layout-section" -->
## CI/CD
<p class="subtitle">ワークフロー設計・Secrets・自動デプロイ</p>

---

<!-- .slide: class="layout-section" -->
## Database Basics
<p class="subtitle">RDB/NoSQL・スキーマ設計・インデックス/トランザクション</p>

---

<!-- .slide: class="layout-section" -->
## Streamlit
<p class="subtitle">社内ツール/ダッシュボードの最短プロトタイプ</p>

---

<!-- .slide: class="layout-section" -->
## Generative AI Fundamentals
<p class="subtitle">LLMの仕組み・トークン/Attentionまで</p>

---

<!-- .slide: class="layout-section" -->
## Generative AI in Practice
<p class="subtitle">性能ベンチ比較・ユースケース・ガードレール</p>

---

<!-- .slide: class="layout-section" -->
## Wrap-up / Next Steps
<p class="subtitle">今日の要点・次に学ぶ順番・実務への接続</p>
