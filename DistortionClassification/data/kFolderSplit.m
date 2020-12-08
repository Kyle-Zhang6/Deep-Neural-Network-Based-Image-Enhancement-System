function suc = kFolderSplit(folderPath,fix,k)
    
    fileFolder = fullfile(folderPath);
    dirOutput = dir(fullfile(fileFolder,['*.',fix]));
    fileNameList = {dirOutput.name};
    size = length(fileNameList);
    fileNameList = fileNameList(randperm(size));
    
    sub_size = floor(size/k);
    for i = 0:1:k-1
        start_ind = sub_size*i + 1;
        end_ind = sub_size*(i+1);
        if i==k-1
            end_ind = size; 
        end
        subset = fileNameList(start_ind:end_ind);
        
        subset_dir = [folderPath,'/folder',num2str(i)];
        mkdir(subset_dir);
        process = 0;
        for img_name = subset
            img_path = [folderPath,'/',img_name{:}];
            %img_out_path = [subset_dir,'/',img_name{:}];
            movefile(img_path,subset_dir);
            fclose('all');
            process = process + 1;
            fprintf('Folder%d Process: %d/%d\n',i,process,length(subset));
        end
    end
    fprintf('\nDone!\n\n');
    suc = true;
end

