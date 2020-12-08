function [img_out] = distortionGenerator(img,type,level)
% Function to generate distorted images with three different distortion
% types: motion-blur, gaussian-noise and JPEG-compression
%   img  : input prestine image
%   type : [0,1,2] -> [motion-blur, gaussian-noise, JPEG-compression]
%   level: [1,2,3,4,5]
%   im_out: output distorted image

blur_len = [3,5,10,15,20];
jpeg_level = [43,12,7,4,0];
wn_level = [-12.5,-10,-7.5,-5.5,-3.5];

% Motion Blur
if type==0
    angle = rand()*360;
    h = fspecial('motion',blur_len(level),angle);
    img_out = imfilter(img,h);
    
elseif type==1  % Gaussian Noise
    temp = rgb2ycbcr(img);
    temp(:,:,1) = imnoise(temp(:,:,1),'gaussian',0,2^(wn_level(level)));
    img_out = ycbcr2rgb(temp);
    % img_out = imnoise(img,'gaussian',0,2^(wn_level(level)));
    
elseif type==2
    imwrite(img,'temp.jpg','quality',jpeg_level(level));
    img_out = imread('temp.jpg');
    delete('temp.jpg');
end
end

