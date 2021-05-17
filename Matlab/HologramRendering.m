function [OutputField] = HologramRendering(E,method,Nx,Ny,pasx,pasy,lambda,z)

x(1:Nx)=(((1:Nx)-1)-round(Nx/2))*pasx; %Valeurs de l'axe x
y(1:Ny)=(((1:Ny)-1)-round(Ny/2))*pasy; %Valeurs de l'axe y
[X,Y]=meshgrid(x,y); %Grille de calcul

    Irest=0; %Initialisation du résultat pour accumulation
        switch method %Choix de la méthode
            case '1FFT'
                phaseQ = exp(1i*pi/(lambda*z)*(X.^2+Y.^2));
                C = E.*phaseQ;
                D = fft2(ifftshift(C'));
                OutputField = D.*exp(-2*1i*pi*z/lambda)./(1i*lambda*z);
            case '2FFT'
                pasu = 1/(Nx*pasx);
                pasv = 1/(Ny*pasy);
                u(1:Nx) = (((1:Nx)-1)-round(Nx/2))*pasu;
                v(1:Ny) = (((1:Ny)-1)-round(Ny/2))*pasv;
                [U,V] = meshgrid(fftshift(u),fftshift(v)); %kx ky
                H = exp(2*1i*pi*z/lambda*sqrt(1-lambda^2*(U).^2-lambda^2*(V).^2));
                
                figure(99);
                imagesc(fftshift(real(H)));
                axis off;
                axis square;
                imwrite(mat2gray(fftshift(real(H))),'t.png');
                
                C11 = fft2(E).*H;
                OutputField = ifft2(C11);
            otherwise
                disp('Méthode de traitement non supportée')
        end%switch method
end
