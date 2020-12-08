
train_loss = TrainingProcess0.TrainLoss;
val_loss = TrainingProcess0.ValLoss;
accuracy = TrainingProcess0.Accuracy .* 100;

figure();
subplot(1,2,1)
plot(train_loss);
hold on;
plot(val_loss);
xlabel('Epoch'),ylabel('Loss'),grid on;
subplot(1,2,2)
plot(accuracy);
xlabel('Epoch'),ylabel('??? / %'),grid on;

% bar(b);
% ylim([95,100]);
% xlabel('????'),ylabel('??? / %')
% grid on;