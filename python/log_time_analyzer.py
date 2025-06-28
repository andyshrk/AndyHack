#!/usr/bin/env python3

import re
import sys
from collections import Counter

def analyze_drm_logs(log_file=None):
    # 如果没有提供文件，则从标准输入读取
    lines = []
    if log_file:
        with open(log_file, 'r') as f:
            lines = f.readlines()
    else:
        print("请从标准输入粘贴日志数据，完成后按Ctrl+D：")
        lines = sys.stdin.readlines()
    
    # 提取时间戳
    timestamps = []
    for line in lines:
        match = re.search(r'\[\s*(\d+\.\d+)\]', line)  # 匹配[数字.数字]格式，允许数字前有空格
        if match:
            timestamps.append(float(match.group(1)))
    
    # 计算时间差（毫秒）
    time_diffs = []
    for i in range(1, len(timestamps)):
        diff = (timestamps[i] - timestamps[i-1]) * 1000  # 转换为毫秒
        # 只保留整数部分
        diff = int(diff)
        time_diffs.append((diff, i))  # 保存时间差和对应的行号
    
    # 统计不同时间差的出现次数
    # 使用整数，不需要处理小数部分
    diff_counter = Counter([diff for diff, _ in time_diffs])
    
    # 按时间差从大到小排序
    sorted_diffs = sorted(diff_counter.items(), key=lambda x: x[0], reverse=True)
    
    # 输出结果
    print("\n时间差统计（从大到小排序）：")
    print("-" * 60)
    print(f"{'时间差(毫秒)':<15}{'出现次数':<15}{'百分比':<15}{'对应的行号'}")
    print("-" * 60)
    
    total_lines = len(time_diffs)
    for diff, count in sorted_diffs:
        # 找出具有该时间差的所有行号
        # 使用整数比较，不需要处理小数部分
        line_numbers = [i+1 for d, i in time_diffs if d == diff]
        # 如果行数超过10行，只显示前10行
        if len(line_numbers) > 10:
            line_numbers_str = ", ".join(map(str, line_numbers[:10])) + "..."
        else:
            line_numbers_str = ", ".join(map(str, line_numbers))
        percentage = (count / total_lines) * 100
        print(f"{diff:<15d}{count:<15}{percentage:.2f}%  {line_numbers_str}")
    
    # 计算统计信息
    if time_diffs:
        min_diff = min(diff for diff, _ in time_diffs)
        max_diff = max(diff for diff, _ in time_diffs)
        avg_diff = sum(diff for diff, _ in time_diffs) / len(time_diffs)
        
        print("\n统计信息：")
        print("-" * 40)
        print(f"最小时间差: {min_diff} 毫秒")
        print(f"最大时间差: {max_diff} 毫秒")
        print(f"平均时间差: {int(avg_diff)} 毫秒")
        print(f"总行数: {len(timestamps)}")
        print(f"时间差总数: {len(time_diffs)}")
        print(f"不同时间差数量: {len(diff_counter)}")
        
        # 计算标准差
        variance = sum((diff - avg_diff) ** 2 for diff, _ in time_diffs) / len(time_diffs)
        std_dev = variance ** 0.5
        print(f"时间差标准差: {int(std_dev)} 毫秒")

if __name__ == "__main__":
    # 检查是否提供了日志文件作为命令行参数
    if len(sys.argv) > 1:
        analyze_drm_logs(sys.argv[1])
    else:
        analyze_drm_logs()