# bert
记录 [天池学习赛](https://tianchi.aliyun.com/competition/entrance/531810/introduction) 使用 bert 进行预训练的过程

## 第一步
生成单词文件和
将比赛的文本转换成需要的格式并分成十份
```
python create_raw_data.py
```

## 第二步
对数据进行 MASK
```
sh create_pretraining_data.sh
```
