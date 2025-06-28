#!/usr/bin/env python3

import re
import sys

def parse_kernel_log(log_content):
    lines = log_content.strip().split('\n')
    mismatched_info = []
    
    # 正则表达式模式
    plane_update_pattern = re.compile(r'.*vop2_plane_atomic_update.*@(\d+)x(\d+).*')
    isr_pattern = re.compile(r'.*vop2_isr.*offset:\s+0x([0-9a-fA-F]+)\s*')
    
    for i in range(len(lines) - 1):
        # 检查当前行是否包含plane_update信息
        plane_match = plane_update_pattern.match(lines[i])
        # 检查下一行是否包含isr信息
        isr_match = isr_pattern.match(lines[i + 1])
        
        if plane_match and isr_match:
            # 从plane_update行提取@后的第一个十进制数字
            x_position = int(plane_match.group(1))
            
            # 从isr行提取offset的十六进制值，并取其底16位
            offset_hex = isr_match.group(1)
            offset_full = int(offset_hex, 16)
            offset_value = offset_full & 0xFFFF  # 取底16位
            offset_hex_16bit = format(offset_value, '04x')  # 格式化为4位十六进制
            
            # 比较两个值是否相等
            if x_position != offset_value:
                # 保存行号、offset底16位的十六进制值和十进制值，以及@后的十进制值
                mismatched_info.append({
                    'line_num': i + 1,  # 行号从1开始计数
                    'offset_hex_16bit': offset_hex_16bit,
                    'offset_dec_16bit': offset_value,
                    'x_position': x_position
                })
    
    return mismatched_info

def main():
    # 从标准输入或文件读取日志内容
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            log_content = f.read()
    else:
        print("请提供日志内容（输入完成后按Ctrl+D）:")
        log_content = sys.stdin.read()
    
    # 解析日志并输出不匹配的信息
    mismatched_info = parse_kernel_log(log_content)
    
    if mismatched_info:
        print("以下行的offset底16位与前一行@后的第一个十进制数字不匹配:")
        # 打印表头
        # 定义列宽
        col1_width = 8  # 行号列宽
        col2_width = 25  # offset底16位列宽
        col3_width = 15  # @后十进制数字列宽
        separator_width = col1_width + col2_width + col3_width + 4  # 加4是因为有3个分隔符和空格
        
        # 打印表头
        print(f"{'行号':<{col1_width}} | {'offset底16位':<{col2_width}} | {'@后十进制数字':<{col3_width}}")
        print("-" * separator_width)
        
        # 打印数据行
        for info in mismatched_info:
            print(f"{info['line_num']:<{col1_width}} | 0x{info['offset_hex_16bit']}({info['offset_dec_16bit']}) | {str(info['x_position']):<{col3_width}}")
            print("-" * separator_width)
    else:
        print("所有检查的行都匹配。")

if __name__ == "__main__":
    main()