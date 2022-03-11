# syukatu_presen
就職作品プレゼンテーション<br>
開発中です

## DEMO
![syupre](https://user-images.githubusercontent.com/70145199/156118456-d729cb2a-e2e3-46e1-bb75-ecc9431550e3.png)

### Prometheusを使って監視中です
![grafana-2022-03-05](https://user-images.githubusercontent.com/70145199/156926322-ac32a01f-ca9d-4a32-980a-c7725e6171f6.png)

### Prometheus / Grafana　の監視項目
#### CPU使用率
##### userのCPU使用率
rate(node_cpu_seconds_total{job="ec2",mode="user"}[5m]) * 100
##### systemのCPU使用率
rate(node_cpu_seconds_total{job="ec2",mode="system"}[5m]) * 100
##### 全体のCPU使用率
100 - (avg by (instance) (rate(node_cpu_seconds_total{job="ec2",mode="idle"}[5m])) * 100)

#### メモリ使用率
##### 全体のメモリ容量
node_memory_MemTotal_bytes{instance="xxxxxx",job="ec2"}/1000000000 - node_memory_MemAvailable_bytes{instance="xxxxxx",job="ec2"}/1000000000
##### 全体のメモリ使用率
node_memory_MemTotal_bytes{instance="xxxxxx",job="ec2"}/1000000000

#### Swap領域の使用率
##### Swapのフリーサイズ
node_memory_SwapFree_bytes{instance="xxxxxx",job="ec2"}
##### Swapのキャッシュサイズ
node_memory_SwapCached_bytes{instance="xxxxxx",job="ec2"}
##### 全体のSwap領域の使用率
node_memory_SwapTotal_bytes{instance="xxxxxx",job="ec2"}

#### ロードアベレージ
##### 直前1分間のロードアベレージ
node_load1
##### 直前5分間のロードアベレージ
node_load5
##### 直前15分間のロードアベレージ
node_load15

#### Prometheusの死活監視
up{instance="localhost:9090", job="prometheus"}

#### Nginxの死活監視
nginx_up

#### httpリクエストの総数
nginx_http_requests_total

## Requirement
asgiref==3.4.1<br>
beautifulsoup4==4.10.0<br>
certifi==2021.10.8<br>
cffi==1.15.0<br>
charset-normalizer==2.0.7<br>
cryptography==35.0.0<br>
defusedxml==0.7.1<br>
Django==3.2.9<br>
django-allauth==0.46.0<br>
django-baton==2.2.3<br>
django-environ==0.8.1<br>
idna==3.3<br>
oauthlib==3.1.1<br>
Pillow==8.4.0<br>
psycopg2-binary==2.9.2<br>
pycparser==2.21<br>
PyJWT==2.3.0<br>
python3-openid==3.2.0<br>
pytz==2021.3<br>
requests==2.26.0<br>
requests-oauthlib==1.3.0<br>
soupsieve==2.3.1<br>
sqlparse==0.4.2<br>
urllib3==1.26.7<br>
