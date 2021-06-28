%TEST OEIL 
OriginDirectory = './';
CurrentImageName = '210211_BAE0275_OD-2_64img.holo';

%CurrentImageName = 'worm2_z0-05_XY_D_2048_2048_8bit_e.raw';
CurrentImage = double(Read_Holo(CurrentImageName));
ImageArraySize = [size(CurrentImage,1),size(CurrentImage,2)];
Nx = ImageArraySize(1);
Ny = ImageArraySize(2);

Image = zeros(Ny,Nx,64);

for i=1:64
    Image(:,:,i)=rot90(fliplr(CurrentImage(:,:,i)));
end

Jk = ones(Ny,Nx,64);
Hk = ones(Ny,Nx,64); % Ce tableau permet de stocker les images une fois traitées
H = zeros(Ny,Nx,'double');
SH = ones(Ny,Nx,64);


% % Première technique de démodulation temporelle par différence d'images

% tab_z = linspace(0.35,0.42,10);
% % tab_z = 0.005
% for z = tab_z
%     for i = 1:63
%         Jk(:,:,i) = Image(:,:,i+1) - Image(:,:,i);
%         Hk(:,:,i) = HologramRendering(Jk(:,:,i),'1FFT',Nx,Ny,12e-6,12e-6,852e-9,z);
%         DisplayedImage = abs(Hk(:,:,i));
%         H = H + DisplayedImage;
%     end
%     
%     figure(1)
%     imagesc(H);
%     axis image;
%     axis off;
%     colormap(gray.^0.5);
%     title('reconstructed hologram');
%     pause(0.01);
% end


%Seconde technique de démodulation temporelle avec une fft temporelle


Z = linspace(0.34,0.45,20);
%for z = Z

n = max([size(Image,1) size(Image,2)]);
img = zeros(n,n,1); 
Hk = zeros(n,n,size(Image,3));
    for i = 1:64
        img(1:size(Image,1),1:size(Image,2)) = Image(:,:,i);
        Hk(:,:,i) = HologramRendering(img,'1FFT',size(img,1),size(img,2),12e-6,12e-6,852e-9,0.38);
    end
    SH = fft(Hk,[],3);
   
%     A = linspace(15,49,35);
%     for i = A
% 
%         DisplayedImage = abs(SH(:,:,i));
%         H = H + DisplayedImage;
%     end 

figure(1);
imagesc(rot90(fftshift(mean(abs(SH(:,:,4:60)),3))));
axis image;
axis off;
colormap(gray.^0.5);
title(sprintf('Final Reconstructed Hologram %.1f',i));


%end
