# limbo-verification
Stake.com limbo verification

# verification

- 1: serverSeed = 服务器种子
- 2: serverSeed_SHA256 = 服务器种子（散列化）
- 3: clientSeed = 客户端种子
- 4: nonce = 随机数
- 5: cursor = 游标（碰撞算法 默认为 0 ）

最终哈希碰撞 计算公式 ：16777216 / (3039525 + 1) * (1 - 0.01) = 5.464484870338335

print(得出结果：5.464484870338335)
