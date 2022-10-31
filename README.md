# サーバーサイドのB
## 実行方法
    プロジェクトディレクトリで
    $docker build -t back_B_image .
    $docker container run -d -p 8000:8000 back_B_image