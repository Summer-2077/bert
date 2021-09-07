# bert
pretrain a bert_mini

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
