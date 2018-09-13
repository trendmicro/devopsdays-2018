# [DevOpsDays Taipei 2018] GitOps - 從 Git 出發

讓我們用 DevOps 的方法，交換 DevOps 的想法。

Demo 網址：https://trendmicro.github.io/devopsdays-2018/

[活動已結束，謝謝大家！]


## 活動說明

透過幾個簡單的 Git 操作，將你對 DevOps 的想法經過 CI/CD 的流程，傳達到大家面前 ：）

- 活動時間：9/11 ~ 9/12 16:00 截止
- 活動獎品：完成規定任務並經工作人員驗證者可獲得「趨勢科技三頭數據線」一組。

## 活動流程

1. 請 **Fork** 此 [專案](https://github.com/trendmicro/devopsdays-2018) 回自己的 GitHub 帳號下。

2. 在 `messages` 這個資料夾下面新增一個以自己 GitHub `username` 為名稱的 YAML 檔案（ex: iamusername.yml）。

3. 在此 YAML 檔案中，以不違反 [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) 的方式留下 `displayname` 和 `message` （其他項目皆為自由分享）。

```
---
  displayname: SRE
  message: Hope is not a strategy.
  skills:
      - python
      - perl
      - c++
  tools: 
      - Puppet
      - Jenkins
      - Graphite
```

4. 完成後請發 pull request 回原專案 `trendmicro/devopsdays-2018`，我們會自動驗證以下項目：
- 只有新增並修改自己的 YAML 檔案
- YAML 檔名與 username 一致
- 可以正常讀取 YAML 檔案並取得 `displayname` 和 `message` 資訊

5. 如果驗證成功，等待數秒鐘則會自動 merge。不成功的話，請確定是否符合上述規則並 close pull request，待修改完成後 reopen pull request。（如果持續不成功的話，請洽現場趨勢科技攤位處理。）

6. 大功告成！感謝您的參與～請前往 [Demo 網站](https://trendmicro.github.io/devopsdays-2018/) 三分鐘左右就可以看到自己的留言囉!

7. 領獎方式：<br>
    * 確認在我們的 Demo 網站上有看到您的留言和署名<br>
    * 請在手機登入您的 GitHub 帳號，並讓攤位工作人員確定留言者為您本人<br>


## 注意事項

本活動的目的在於交流，如有不適當的言語，或是違反資訊安全的行為，主辦單位有權取消獲獎資格。
