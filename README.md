# rime-moetaigi 萌台語: 基於萌典 API 的 RIME 臺語輸入法

使用注音符號輕鬆輸入台語。萌台語是使用[中州韻輸入法引擎 (Rime)](https://rime.im/) 客製化與[萌典 API](https://www.moedict.tw/about.html) 取得的詞條來源建立的臺語輸入法。詞條與拼音來源為《臺灣閩南語常用詞辭典》。

![你嘛來試看覓](doc/images/moetaigi-try.gif)

## 特點

1. **精確**
漢字與對應發音以《臺灣閩南語推薦用字》為基準，可依照聲調精確打字。

![骨力](doc/images/moetaigi_eg1.gif)

2. **快速**
支援簡拼 (不打聲調或只打聲符) 輸入，內建 AI 更會記錄使用者的常用字，多打速度就越快。

![假鬼假怪](doc/images/moetaigi_eg2.gif)

3. **詳盡**
與萌典收錄詞條同步，透過 API 收錄兩萬多筆台語字詞。
4. **學習**
只會念但不知道漢字怎麼寫？使用萌台語拼出來找漢字！字詞拼音與萌典相同，保證在字典查到的條目可以用此輸入法打出來！

![拄才我看著虼蚻](doc/images/moetaigi_eg3.gif)

5. **開源**
開放原始碼並使用 CC0 公眾領域授權，任何人都可以不受限制地使用或改進此作品。

## 安裝

1. 安裝 [Rime](https://rime.im/) 的發行版
2. 下載 [rime-moetaigi](https://github.com/whyjz/rime-moetaigi/archive/refs/heads/main.zip)
3. 解壓縮後找到 `moetaigi-tsuim.schema.yaml`、`tsuim.yaml`，和 `moetaigi.dict.yaml` 三個檔案，複製到 `%APPDATA%\Rime` 資料夾底下 (非 Windows 作業系統請參考 [用戶文件夾位置](https://github.com/rime/home/wiki/UserData))。
4. 重新佈署 Rime 以後，進入輸入法設定啟用「萌台語-注音」(如下圖)。

![啟用「萌台語-注音」](doc/images/rime-moetaigi-install.png)

## 使用說明

- `ctrl + ~`: 切換至萌台語-注音輸入法或 Rime 提供的其他輸入法
- `shift`: 切換漢字 / 英數輸入
- `空白鍵` 或 `Enter`: 從候選字視窗選字
- 注音符號的鍵盤配置請參考下圖。注意深綠色的注音需搭配 `shift` 輸入；例如 `shift + d` 可以輸入「ㄫ」。符號代表的發音請參考臺語注音符號的[維基說明](https://zh.wikipedia.org/wiki/%E8%87%BA%E7%81%A3%E6%96%B9%E9%9F%B3%E7%AC%A6%E8%99%9F)。

![鍵盤配置](doc/images/Keyboard_layout_Tsuim.png)
*萌台語-注音輸入法的注音配置。**淺綠色底的按鍵**：與大千式注音鍵盤相同或發音相似的注音。**紅色底的按鍵**：與大千式注音鍵盤不同的注音。**黃色底的按鍵**：聲調符號。 修改自 [Sakurambo](https://commons.wikimedia.org/wiki/File:Keyboard_layout_Zhuyin.svg) 的作品。本作品以 [CC BY-SA 4.0 授權](https://creativecommons.org/licenses/by-sa/4.0/deed.zh_TW)發布。*

詳細的說明文檔 (之後補上)

## 鳴謝與資料來源

感謝以下專案與資料來源，以及背後的作者與貢獻者們，讓本輸入法得以奠基與實現：

1. [Rime 中州韻輸入法引擎](https://rime.im/) ([佛振](https://github.com/lotem))
2. [萌典](https://www.moedict.tw/)與[萌典 API](https://github.com/g0v/moedict-webkit) ([唐鳳](https://github.com/audreyt))
3. [《臺灣閩南語常用詞辭典》](http://twblg.dict.edu.tw/)，使用 [CC BY-ND 3.0 臺灣授權](http://twblg.dict.edu.tw/holodict_new/compile1_6_1.jsp)
4. 感謝夢生 (Yuh-ru/Dyertung) 的母錄 (blog/部落) 在隨意窩上發表的[部育部臺灣閩南語常用詞辭典語詞字頻表](https://blog.xuite.net/hn88196555/twblog/563937744)。
5. 感謝以下 Rime 的官方/客製化輸入法 schema 為本專案的開發提供了範本與靈感：
   - [『注音 洋蔥』](https://deltazone.pixnet.net/blog/post/264319309-%E9%BC%A0%E9%AC%9A%E7%AE%A1%E6%B3%A8%E9%9F%B3%E6%96%B9%E6%A1%88---%E7%AC%A6%E5%90%88%E4%B8%80%E8%88%AC%E6%B3%A8%E9%9F%B3%E4%BD%BF%E7%94%A8%E8%80%85%E7%BF%92%E6%85%A3%E8%A8%AD)(L'Étranger Onion)
   - [『Rime 注音輸入方案』](https://github.com/rime/rime-bopomofo)(佛振)
   - [『意傳台文輸入法』](https://github.com/i3thuan5/rime-taigi)(ÌTHUÂNKHOKI 意傳科技)
   - [『RIME 台語輸入方案』](https://github.com/glll4678/rime-taigi)(莊銘彥)

<!-- 昆蟲 https://www.facebook.com/morethandee/photos/a.369345609816495/1097476730336709/?type=3 -->

## 授權條款

![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)

在本作品中，除了少數以其他授權發佈的圖片外，作者鄭懷傑 (Whyjay Zheng) 已在法律許可的範圍內，拋棄該著作依著作權法所享有之權利，包括所有相關與鄰接的法律權利，並宣告將該著作貢獻至公眾領域。你可以複製、修改、發布或展示此作品，亦可進行商業利用，完全不需要經過許可。更多資訊可參閱 [LICENSE](LICENSE) 檔或[這裡](https://creativecommons.org/publicdomain/zero/1.0/deed.zh_TW)。

對於以其他授權發佈的圖片，您可以在圖片說明文字中找到授權條款。

## 如何參與開發

萌台語歡迎各路英雄一同參與開發！文檔錯字、補充說明，乃至程式碼改進、擴增新功能... 不管您想到的是什麼，您可以：

1. 開 Issue 提出您的問題與建議，或是未來開發的想法
2. 隨時送一個 PR 過來，一起完善萌台語輸入法！

給開發者參考的文件 (之後補上)