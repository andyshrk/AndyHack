#!/usr/bin/env python
import sys
import re

def analyze_fence_lifecycle(filename):
    try:
        fence_data = {}  # 存储每个fence的数据 {seqno: {'init': timestamp, 'signaled': timestamp}}
        
        with open(filename, 'r') as file:
            for line in file:
                # 解析时间戳
                time_match = re.search(r'\s+\d+\.\d+:', line)
                if not time_match:
                    continue
                timestamp = float(time_match.group().strip().rstrip(':'))
                
                # 解析seqno
                seqno_match = re.search(r'seqno=(\d+)', line)
                if not seqno_match:
                    continue
                seqno = int(seqno_match.group(1))
                
                # 判断事件类型
                if 'dma_fence_init' in line:
                    if seqno not in fence_data:
                        fence_data[seqno] = {'init': timestamp}
                elif 'dma_fence_signaled' in line:
                    if seqno in fence_data and 'init' in fence_data[seqno]:
                        fence_data[seqno]['signaled'] = timestamp

        # 分析时间差
        print("异常Fence时间差分析结果（>16.7ms*2）：")
        print("-" * 50)
        for seqno, data in sorted(fence_data.items()):
            if 'init' in data and 'signaled' in data:
                diff_ms = (data['signaled'] - data['init']) * 1000
                if diff_ms > 16.7 * 2:
                    print(f"Fence seqno={seqno}: {diff_ms:.3f} ms")
                    print(f"    Init:     {data['init']:.6f}")
                    print(f"    Signaled: {data['signaled']:.6f}\n")

    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}")
    except Exception as e:
        print(f"处理过程中出现错误：{str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: fence_analyzer.py <log文件路径>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    analyze_fence_lifecycle(log_file)
