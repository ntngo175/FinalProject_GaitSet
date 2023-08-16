import torch
import torch.nn.functional as F
import numpy as np
import pandas as pd
import pickle


def cuda_dist(x, y):
    x = torch.from_numpy(x).cuda()
    y = torch.from_numpy(y).cuda()
    dist = torch.sum(x ** 2, 1).unsqueeze(1) + torch.sum(y ** 2, 1).unsqueeze(
        1).transpose(0, 1) - 2 * torch.matmul(x, y.transpose(0, 1))
    dist = torch.sqrt(F.relu(dist))
    return dist


def evaluation(probe, gallery, valid=False):
    probe_feature, seq_id, _, _ = probe
    gallery_feature, _, _, gait_id = gallery
    seq_id = np.array(seq_id)
    gait_id = np.array(gait_id)
    
    # print('c', len(c))
    # print('gait_id', len(gait_id))


    dist = cuda_dist(probe_feature, gallery_feature)

    dist = dist.cpu().numpy()
    idx = np.argmin(dist, axis=1)
    # print('idx: {}'.format(idx))
    
    seq_gait_id = gait_id[idx]
    s=[]
    dic = {}
    for i in range(len(seq_id)):
        s.append([seq_id[i], seq_gait_id[i]])
        dic[seq_id[i]] = seq_gait_id[i]
        
    if valid:
        f = open('../dataset/labels.pkl', 'rb')
        labels = pickle.load(f)
        print(labels)
        f.close()
        
        acc = 0
        for i, id_ in enumerate(labels[0]):
            if id_ in dic.keys():
                if dic[id_]==labels[1][i]:
                    acc += 1
        return acc / len(labels[0])  
    else:
        print(s)
        print(s[0])
        print("Day la nguoi thu", s[0][1])
        # return s[0][0], s[0][1]
        return s[0][1]
    '''
    print('seq_gait_id: {}'.format(seq_gait_id))
    human_id = seq_gait_id[0]
    # result = 'Nhận dạng sai'
   
    # if seq_gait_id[i] == human_id and i == 1:
    #   result = human_id
    print('Day la nguoi ', seq_gait_id[0])
    '''
        
    

    # s = []
    # dic = {}
    # # print('seq_id: ', len(seq_id))

    # # seq_id: nhãn chưa biết
    # # seq_hait_id: danh sách nhãn đã biết sắp xếp theo thứ tự
    # for i in range(len(seq_id)):
    #   if s[i] == temp and i == 11:
    #     result = human_id
    #     break

    #       return result
    #     s.append([seq_id[i], seq_gait_id[i]])
    #     dic[seq_id[i]] = seq_gait_id[i]
    #     print('dic: {}'.format(dic))


    # if valid:
    #     f = open('../dataset/labels.pkl', 'rb')
    #     labels = pickle.load(f)
    #     f.close()

    #     acc = 0
    #     for i, id_ in enumerate(labels[0]):
    #         if id_ in dic.keys():
    #             if dic[id_] == labels[1][i]:
    #                 acc += 1
    #     return acc / len(labels[0])
    # else:
        # print('s', s)
        # print(s[0])
        # print("videoID", s[0][0], "subjectID", s[0][1])
        # return s[0][0], s[0][1]
        # return s[0][1]
    # print('pid_list: {}'.format(len(dic)))
        # submission = pd.DataFrame(s, columns=['videoID', 'subjectID'])
        # submission.to_csv('submission.csv', index=False)
