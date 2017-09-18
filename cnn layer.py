layer {
  name: "conv1" # 名稱：conv1
  type: "Convolution" # 類型：卷積層
  bottom: "data" # 輸入層：數據層
  top: "conv1" # 輸出層：卷積層1
  # 濾波器（filters）的學習速率因子和衰減因子
  param { lr_mult: 1 decay_mult: 1 }
  # 偏置項（biases）的學習速率因子和衰減因子
  param { lr_mult: 2 decay_mult: 0 }
  convolution_param {
    num_output: 96 # 96個濾波器（filters）
    kernel_size: 11 # 每個濾波器（filters）大小為11*11
    stride: 4 # 每次濾波間隔為4個像素
    weight_filler {
      type: "gaussian" # 初始化高斯濾波器（Gaussian）
      std: 0.01 # 標準差為0.01， 均值默認為0
    }
    bias_filler {
      type: "constant" # 初始化偏置項（bias）為零
      value: 0
    }
  }
}
