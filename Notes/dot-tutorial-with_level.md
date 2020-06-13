## level 1
### 基本语法
```gv
digraph G {

    /* Entities */
    shortName [label="shortName", shape="square"]
    
    /* Relationships */
    F1 -> shortName[label=".63"]

    /* Ranks */
    { rank=same; shortName; };
}
```
有向图
```gv
graph G {

    /* Entities */
    shortName [label="shortName", shape="square"]
    
    /* Relationships */
    F1 -- shortName[label=".63"]

    /* Ranks */
    { rank=same; shortName; };
}
```

无向图

节点

边


## level 2
属性

## level 3
特别属性