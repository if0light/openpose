import collections


def load_state(net, checkpoint):
    source_state = checkpoint['state_dict'] # 从检查点中提取模型的状态字典（即预训练权重
    target_state = net.state_dict()# 获取目标网络的状态字典（即当前网络的权重）
    new_target_state = collections.OrderedDict() # 创建一个有序字典用于存储新的目标状态
    for target_key, target_value in target_state.items(): # 遍历目标网络的所有参数
        if target_key in source_state and source_state[target_key].size() == target_state[target_key].size():
            new_target_state[target_key] = source_state[target_key]
        else:
            new_target_state[target_key] = target_state[target_key]
            print('[WARNING] Not found pre-trained parameters for {}'.format(target_key))

    net.load_state_dict(new_target_state)


def load_from_mobilenet(net, checkpoint):
    source_state = checkpoint['state_dict']
    target_state = net.state_dict()
    new_target_state = collections.OrderedDict()
    for target_key, target_value in target_state.items():
        k = target_key
        if k.find('model') != -1:
            k = k.replace('model', 'module.model')
        if k in source_state and source_state[k].size() == target_state[target_key].size():
            new_target_state[target_key] = source_state[k]
        else:
            new_target_state[target_key] = target_state[target_key]
            print('[WARNING] Not found pre-trained parameters for {}'.format(target_key))

    net.load_state_dict(new_target_state)
