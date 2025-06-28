#!/usr/bin/env python3
import re
import sys

def extract_timestamp(line):
    """
    从日志行中提取时间戳
    
    参数:
        line (str): 日志行
        
    返回:
        str: 时间戳字符串（带方括号），如果未找到返回空字符串
    """
    # 匹配内核日志时间戳格式 [数字.数字]
    kernel_timestamp_match = re.search(r'^\s*(\[\s*\d+\.\d+\])', line)
    if kernel_timestamp_match:
        # 去掉方括号内的空格
        timestamp_with_spaces = kernel_timestamp_match.group(1)
        # 提取数字部分
        number_match = re.search(r'\[(\s*\d+\.\d+)\]', timestamp_with_spaces)
        if number_match:
            number_part = number_match.group(1).strip()
            return f"[{number_part}]"
        return timestamp_with_spaces
    
    # 尝试匹配其他常见的时间戳格式
    timestamp_match = re.search(r'^(\[\s*\d{2}:\d{2}:\d{2}\.\d{3}\s*\])|^(\d{2}:\d{2}:\d{2}\.\d{3})|^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})', line)
    if timestamp_match:
        # 返回第一个非None的匹配组
        for group in timestamp_match.groups():
            if group:
                # 如果时间戳有方括号，去掉方括号内的空格
                if group.startswith('[') and group.endswith(']'):
                    # 提取方括号内的内容并去除空格
                    content_match = re.search(r'\[(\s*.*?\s*)\]', group)
                    if content_match:
                        content = content_match.group(1).strip()
                        return f"[{content}]"
                    return group
                # 如果时间戳没有方括号，添加方括号
                else:
                    return f"[{group}]"
    return ""

def extract_coordinates(line):
    """
    从日志行中提取坐标信息
    
    参数:
        line (str): 日志行
        
    返回:
        tuple: (cluster_coord, priv_coord) 坐标字符串，如果未找到返回(None, None)
    """
    # 提取Cluster0-win0部分@符号后的坐标
    cluster_match = re.search(r'Cluster0-win0\[[^\]]*@([\dx]+)\]', line)
    cluster_coord = cluster_match.group(1) if cluster_match else None
    
    # 提取priv部分最后一个空格后的坐标
    priv_match = re.search(r'priv\[[^\]]* ([\dx]+)\]', line)
    priv_coord = priv_match.group(1) if priv_match else None
    
    return cluster_coord, priv_coord

def analyze_kernel_logs(file_path=None, log_content=None):
    """
    分析内核日志，找出当前行priv部分和前一行Cluster0-win0部分标识的坐标不相同的行
    
    参数:
        file_path (str, optional): 日志文件路径
        log_content (str, optional): 日志内容字符串
        
    返回:
        list: 包含所有满足条件的信息，每项包含行号、前一行、当前行、前一行坐标和当前行坐标
    """
    result = []
    lines = []
    
    # 获取日志内容
    if file_path:
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"错误: 文件 '{file_path}' 未找到")
            return result
        except Exception as e:
            print(f"处理文件时出错: {e}")
            return result
    elif log_content:
        lines = [line.strip() for line in log_content.split('\n') if line.strip()]
    else:
        print("错误: 需要提供文件路径或日志内容")
        return result
    
    # 分析日志行
    for i in range(1, len(lines)):
        # 提取当前行和前一行的坐标
        prev_cluster_coord, _ = extract_coordinates(lines[i-1])
        _, current_priv_coord = extract_coordinates(lines[i])
        
        # 比较当前行的priv坐标与前一行Cluster0-win0坐标
        if current_priv_coord and prev_cluster_coord and current_priv_coord != prev_cluster_coord:
            # 提取当前行的时间戳
            current_timestamp = extract_timestamp(lines[i])
            
            result.append({
                'line_num': i + 1,  # 行号从1开始计数
                'timestamp': current_timestamp,
                'prev_line': lines[i-1],
                'current_line': lines[i],
                'prev_coords': prev_cluster_coord,
                'current_coords': current_priv_coord
            })
    
    return result

# 样例日志数据
SAMPLE_LOG = """[   71.274107] rockchip-vop2 fe040000.vop: [drm:vop2_plane_atomic_update] vp0 update Cluster0-win0[64x64->64x64@0x0] priv[0x00fda000 953x536] fmt[AB24_AFBC] addr[0x0000000000fef000] 
[   71.274590] rockchip-vop2 fe040000.vop: [drm:vop2_plane_atomic_update] vp0 update Cluster0-win0[64x64->64x64@0x200] priv[0x00fda000 953x536] fmt[AB24_AFBC] addr[0x0000000000fef000] 
[   71.290922] rockchip-vop2 fe040000.vop: [drm:vop2_plane_atomic_update] vp0 update Cluster0-win0[64x64->64x64@6x200] priv[0x00fef000 0x200] fmt[AB24_AFBC] addr[0x0000000000fef000] 
[   71.307133] rockchip-vop2 fe040000.vop: [drm:vop2_plane_atomic_update] vp0 update Cluster0-win0[64x64->64x64@12x200] priv[0x00fef000 6x200] fmt[AB24_AFBC] addr[0x0000000000fef000] 
[   71.323347] rockchip-vop2 fe040000.vop: [drm:vop2_plane_atomic_update] vp0 update Cluster0-win0[64x64->64x64@18x200] priv[0x00fef000 12x200] fmt[AB24_AFBC] addr[0x0000000000fef000] 
[   71.339788] rockchip-vop2 fe040000.vop: [drm:vop2_plane_atomic_update] vp0 update Cluster0-win0[64x64->64x64@24x200] priv[0x00fef000 18x200] fmt[AB24_AFBC]
"""

def main():
    # 从标准输入或文件读取日志内容
    log_content = None
    file_path = None
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    elif not sys.stdin.isatty():  # 检查是否有管道输入
        print("从标准输入读取日志内容...")
        log_content = sys.stdin.read()
    else:
        print("未提供日志文件，使用内置样例数据进行演示...")
        log_content = SAMPLE_LOG
        
    # 解析日志并输出不匹配的信息
    mismatched_info = analyze_kernel_logs(file_path, log_content)
    
    # 统计不匹配的行数
    mismatched_count = len(mismatched_info)
    
    if mismatched_info:
        print(f"以下行的priv坐标与前一行Cluster0-win0坐标不匹配 (共 {mismatched_count} 行):")
        # 定义列宽
        col1_width = 6   # 行号列宽
        col2_width = 15  # 时间戳列宽
        col3_width = 18  # 前一行坐标列宽
        col4_width = 18  # 当前行坐标列宽
        
        # 计算分隔线长度
        separator_width = col1_width + col2_width + col3_width + col4_width + 6  # 加6是因为有4个分隔符和空格
        
        # 创建格式化模板
        row_format = "{:<" + str(col1_width) + "}|{:<" + str(col2_width) + "}|{:<" + str(col3_width) + "}|{:<" + str(col4_width) + "}"
        
        # 打印表头
        print(row_format.format("行号", " 时间戳", " 前一行坐标", " 当前行坐标"))
        print("-" * separator_width)
        
        # 打印数据行
        for info in mismatched_info:
            line_num_str = str(info['line_num'])
            timestamp_str = info['timestamp'] if info['timestamp'] else "无时间戳"
            print(row_format.format(line_num_str, " " + timestamp_str, " " + str(info['prev_coords']), " " + str(info['current_coords'])))
            print("-" * separator_width)
            
            # 可选：打印详细信息
            # print("前一行:")
            # print(info['prev_line'])
            # print("当前行:")
            # print(info['current_line'])
            # print()
        
        # 在结尾再次显示统计信息
        print(f"总计: {mismatched_count} 行不匹配")
    else:
        print("所有检查的行的坐标都匹配。")

if __name__ == "__main__":
    main()
