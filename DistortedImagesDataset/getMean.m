clear
clc

folderPath = './distorted_images';
fix = 'bmp';

fileFolder = fullfile(folderPath);
dirOutput = dir(fullfile(fileFolder,['*.',fix]));
fileNameList = {dirOutput.name};

sum_list = zeros(length(fileNameList),3);
pixel_num_list = zeros(1,length(fileNameList));
i = 1;
for p = fileNameList
   img_path = [folderPath,'/',p{:}] ;
   img = imread(img_path);
   img_sum = sum(sum(img));
   sum_list(i,:) = img_sum;
   [w,h,c] = size(img);
   pixel_num_list(i) = w*h;
   
   fprintf('Process: %d/%d\n',i,length(fileNameList));
   i = i+1;
end
mean_rgb = mean(sum_list,1)./mean(pixel_num_list);
fprintf('\nDone!\n\n')