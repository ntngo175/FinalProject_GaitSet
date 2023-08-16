conf = {
    "WORK_PATH": "/content/drive/MyDrive/FinalGaitSet/work1",
    "CUDA_VISIBLE_DEVICES": "0",
    "data": {
        'dataset_path': "/content/drive/MyDrive/FinalGaitSet/RealData",
        'resolution': '64',
        'dataset': 'CASIA-B',
        # In CASIA-B, data of subject #5 is incomplete.
        # Thus, we ignore it in training.
        # For more detail, please refer to
        # function: utils.data_loader.load_data
        'pid_num': 73,
        'pid_shuffle': False,
    },
    "probe": {
        'dataset_path': "/content/drive/MyDrive/FinalGaitSet/dataset/after_test_probe",## 'dataset_path': "../dataset/test_probe_pre",
        'resolution': '64',
        'dataset': 'CASIA-B',
        'pid_num': 1,
        'pid_shuffle': False,
    },
    "gallery": {
        'dataset_path': "/content/drive/MyDrive/FinalGaitSet/gallery",
        'resolution': '64',
        'dataset': 'CASIA-B',
        'pid_num': 7,
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,
        'lr': 1e-4,
        'hard_or_full_trip': 'full',
        'batch_size': (8, 16),
        'restore_iter': 0,
        'total_iter': 10000,
        'margin': 0.2,
        'num_workers': 0,
        'frame_num': 30,
        'model_name': 'GaitSet',
    },
}
