clear
clc

folderPath = './distorted_images';
fix = 'bmp';

fileFolder = fullfile(folderPath);
dirOutput = dir(fullfile(fileFolder,['*.',fix]));
fileNameList = {dirOutput.name};
mean_rgb = [0.4955,0.4544,0.4145];

var_list = zeros(length(fileNameList),3);
pixel_num_list = zeros(1,length(fileNameList));
i = 1;
for p = fileNameList
   img_path = [folderPath,'/',p{:}] ;
   img = double(imread(img_path))/255;
   img_var = [0,0,0];
   for j = 1:3
       img_var(j) = sum((img(:,:,j)-mean_rgb(j)).^2,'all');
   end   
   var_list(i,:) = img_var;
   [w,h,c] = size(img);
   pixel_num_list(i) = w*h;
   
   fprintf('Process: %d/%d\n',i,length(fileNameList));
   i = i+1;
end
var_rgb = sqrt(mean(var_list,1)./mean(pixel_num_list));
fprintf('\nDone!\n\n')