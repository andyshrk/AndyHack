#!/usr/bin/env python
import sys
import re

def calculate_timestamp_diff(filename):
    try:
        # 读取日志文件
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # 提取时间戳
        timestamps = []
        for line in lines:
            if line.strip():  # 跳过空行
                # 使用更精确的正则表达式匹配时间戳
                match = re.search(r'\s+\d+\.\d+:', line)
                if match:
                    # 去除冒号并转换为浮点数
                    timestamp = float(match.group().strip().rstrip(':'))
                    timestamps.append(timestamp)
        
        # 计算并打印时间差
        print("异常时间差分析结果（>16.7ms 或 <0ms）：")
        print("-" * 50)
        for i in range(1, len(timestamps)):
            diff_ms = (timestamps[i] - timestamps[i-1]) * 1000
            if diff_ms > 16.7:
                print(f"{i} -> {i+1}: {diff_ms:.3f} ms")
            elif diff_ms < 0:
                print(f"{i} -> {i+1}: {diff_ms:.3f} ms")
                print(f"    时间戳: {timestamps[i-1]:.6f} -> {timestamps[i]:.6f}")
            
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}")
    except Exception as e:
        print(f"处理过程中出现错误：{str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: timestamp_diff.py <log文件路径>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    calculate_timestamp_diff(log_file)
