%dummy text
z = 0.06;
ImageArraySize = [2048,2048];
Nx = ImageArraySize(1);
Ny = ImageArraySize(2);

pathparts = strsplit(pwd,filesep);

if ~(strcmp(pathparts(end-1), "HologramRendering"))
    if ~(strcmp(pathparts(end), "Matlab"))
     %   disp("Please run this script from HologramRendering/Matlab/")
     f = msgbox("Please run this script from HologramRendering/Matlab/", "Invalid Folder", "error");
        return
    end
end

OriginDirectory = '../Images/';
CurrentImageName = 'GaborTarget_SingleImage_XY_D_2048_2048_8bit_e.raw';

%CurrentImageName = 'worm2_z0-05_XY_D_2048_2048_8bit_e.raw';



fid = fopen([OriginDirectory,CurrentImageName], 'r');
%fseek(fid,Nshift*Nx*Ny,'bof'); %decalage de Nshift images
CurrentImage = fread(fid,Nx*Ny,'uint8=>uint8');
fclose(fid);

CurrentImage = double(CurrentImage);
CurrentImage = reshape(CurrentImage,Nx,Ny);

figure(1)
imagesc(abs(CurrentImage));
axis image;
axis off;
colormap(gray.^0.5);
title('interferogram');
 
tab_z = linspace(0.01,0.3,10);
% tab_z = 0.005
for pp = 1:length(tab_z)
z = tab_z(pp);
[OutputField] = HologramRendering(CurrentImage,'2FFT',Nx,Ny,5.5e-6,5.5e-6,658e-9,-z);
DisplayedImage = abs(OutputField);
figure(2)
imagesc(DisplayedImage);
axis image;
axis off;
colormap(gray.^0.5);
title('reconstructed hologram');
pause(0.01);
end%pp

figure(3)
imagesc(log(abs(fftshift(fft2(CurrentImage)))));
axis image;
axis off;
colormap(gray.^0.5);
title('Fourier plane');
