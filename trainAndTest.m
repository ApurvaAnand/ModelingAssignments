function[] = trainAndTest(train, test)
missing_imputed=knnimpute(train);
NormTrainData=quantilenorm(missing_imputed);


% for ttest
All=NormTrainData(:,1:27);
AMLTrain=NormTrainData(:,28:39);
[PValues, TScores]=mattest(All,AMLTrain);

% finding significant
significantTrain=PValues<0.01; % put it as 0.01 instead of 0.05
significantTrainIndex=find(significantTrain);

% filtering

% for i=1:1401
% 
% v=significantTrainIndex(i);
% 
% matrix(i,:)=NormTrainData(v,:);
% 
% 
% end

matrixSignific = NormTrainData(significantTrainIndex,:);
matrixSignific = matrixSignific - mean(matrixSignific(:));
matrixSignific = matrixSignific/std(matrixSignific(:));
y = [ones(1,27), zeros(1,12)]'; % All -> 1 and AMLTrain ->0

[B FitInfo] = lassoglm(matrixSignific',y,'binomial','CV',4);
lassoPlot(B,FitInfo,'plottype','CV');

minFeatures = find(B(:,FitInfo.IndexMinDeviance));
%glmMdl = fitglm(matrixSignific(minFeatures,:)', y, 'Link', 'logit');
glmMdl = fitglm(matrixSignific(minFeatures,:)', y);

test = test-mean(test(:));
test = test/std(test(:));
testSignic = test(minFeatures,:);

ypred = predict(glmMdl, testSignic')>0.2

end