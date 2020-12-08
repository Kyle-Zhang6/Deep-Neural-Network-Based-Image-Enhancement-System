clear
clc

path_base = './pristine_images/';
path_fix = '.bmp';

%start_ind = 4501;
%end_ind = 4510;
rand_ind = randperm(4744-1000,100);
ind_rest = 1001:1:4744;
ind_list = ind_rest(rand_ind);

fprintf('Start...\n');
for i = ind_list
    ind = sprintf('%05d',i);
    path = [path_base,ind,path_fix];
    img = imread(path); 
    
    for j = 0:1:2
        for k = 1:1:5
            img_distorted = distortionGenerator(img,j,k); 
            imwrite(img_distorted,['./test_images/',ind,'_0',num2str(j),'_',num2str(k),'.bmp']);
        end
    end
    fprintf('Process: %d/%d...\n',i,length(ind_list));
end
fprintf('\nDone!\n\n');