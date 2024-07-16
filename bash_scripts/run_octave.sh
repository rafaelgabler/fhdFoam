#!/bin/bash

#echo -e "\nenter the path to directory untill the time step you want to view"
#read the_path  #Lê o caminho até a temperatura no passo de tempo escolhido

#echo -e "\nenter the path to directory untill the probe"
#read the_path2  #Lê o caminho até a temperatura descrita na probe

#postProcessing/probes/0/T
script_octave="script_octave.m"

cat > $script_octave << EOF
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% caminhos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

probe = 'postProcessing/probes/0/T'; 	% coloca o caminho de T em probe
WW = 'postProcessing/probes/0/W';
fid2 = '600/T';			% coloca o caminho de T namalha toda em fid2
WW2 = '600/W'


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Abre arquivos e lê %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fid = fopen (probe,'r');	%Abre probe para leitura
fid22 = fopen (fid2, 'r');	%Abre fid2 para leitura
fidW = fopen (WW,'r');	%Abre probe para leitura
fidW22 = fopen (WW2, 'r');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Separa em colunas %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% probe %%%

dados = textscan(fid, '%f %f %f', 'headerlines', 3) %separa as informações das colunas da probe, se tiver mais colunas de T é preciso adicionar mais '%f'
fclose(fid); 			%Fecha fid

%%% perfusão %%%

dadosW = textscan(fidW, '%f %f %f', 'headerlines', 3)

%%% Temperatura ao longo da malha %%%

dados2 = textscan(fid22,'%f', 'headerlines', 23);

fclose (fid22);
n=0;
dados2 = dados2{1}(1:end-n);

%%% perfusão %%%
dadosW2 = textscan(fidW22,'%f', 'headerlines', 23);
dadosW2 = dadosW2{1}(1:end-n);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Estabelece as variáveis %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% probe %%%

tempo = dados{1}; 		
temperatura1 = dados{2};
temperatura2 = dados{3};

%%% perfusão ao longo da malha %%%
W1 = dadosW{2};
W2 = dadosW{3};

% estabelece as características do domínio de cálculo e da malha

xb=0;
xl=0.09;
nx=200;
yb=0;
yl=0.09;
ny=200;

% estabelece x,y e T no gráfico

x=linspace(xb,xl,nx);
y=linspace(yb,yl,ny);
[xx,yy]=meshgrid(x,y);
T = reshape(dados2, [nx, ny]);
W = reshape(dadosW2, [nx, ny]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% plota em gráfico %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%% probe %%%

figure;
plot(tempo, temperatura1, '-o', 'LineWidth', 0.5, 'Markersize', 1);
hold on;
plot(tempo, temperatura2, '-s', 'LineWidth', 0.5, 'Markersize', 1);
xlabel('Tempo (s)');
ylabel('Temperatura (K)');
title('T x t');
legend ('Tumor 1', 'Tumor 2', 'location','southeast');
print('grafico_temperatura.png', '-dpng')

%%% perfusão sanguínea %%%

figure;
plot(tempo, W1, '-o', 'LineWidth', 0.5, 'Markersize', 1);
hold on;
plot(tempo, W2, '-s', 'LineWidth', 0.5, 'Markersize', 1);
xlabel('Tempo (s)');
ylabel('perfusão sanguínea (1/s)');
title('W x t');
legend ('Tumor 1', 'Tumor 2', 'location','southeast');
print('grafico_perfusion.png', '-dpng')

figure;
%plot3(xx,yy,W)
surf(xx,yy,W,'Edgecolor','none')
xlabel('x (m)');
ylabel('y (m)');
zlabel('W (1/s)')
title('Distribution of perfusion in the domain');
rotate3d on;
print('grafico_Wxy', '-dpng')
waitfor(gcf);

%%% Temperatura ao longo da malha %%%
figure;
%plot3(xx,yy,T)
surf(xx,yy,T,'Edgecolor','none')
xlabel('x (m)');
ylabel('y (m)');
zlabel('T (K)')
title('Distribution of temperature in the domain');
rotate3d on;
print('grafico_Txy', '-dpng')
waitfor(gcf);


EOF



echo "Conteúdo do script Octave:"
cat $script_octave

echo "Executando Octave"
octave  $script_octave

if [-f "grafico_temperatura.png"]; then
	echo "Gráfico gerado!"
else
	echo "Erro no gráfico"
fi.
%rm $script_octave
