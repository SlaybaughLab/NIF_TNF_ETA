h = plot(NaN,NaN); %// initiallize plot. Get a handle to graphic object
DATASET1 = [25	54	114	140	174	259	331	421	467	542 744	754	852	1154	1247	1737	2482	2492	2755	2836	3160	3280	3384	3458	3783	3955	3971	4050	4390	4475	4561	4575]; 
DATASET2 = [4.48E-01 2.62E-01	2.20E-01	2.19E-01	1.89E-01	1.88E-01	1.80E-01	1.67E-01	1.54E-01	1.48E-01	1.30E-01	1.22E-01	1.15E-01	1.13E-01	1.10E-01	1.04E-01	1.03E-01	1.00E-01	9.51E-02	9.27E-02	9.03E-02	9.54E-02	9.03E-02	8.49E-02	8.24E-02	8.17E-02	8.16E-02	8.09E-02	8.05E-02	7.53E-02	7.51E-02	7.32E-02];
axis([0 5000 0 0.5]); %// freeze axes
%// to their final size, to prevent Matlab from rescaling them dynamically 

% Create a VideoWriter object to write the video out to a new, different file.
writerObj = VideoWriter('results.mp4');
writerObj.FrameRate = 2;
writerObj.Quality = 100;
open(writerObj);
for ii = 1:length(DATASET1)
    pause(0.5)
    set(h, 'XData', DATASET1(1:ii), 'YData', DATASET2(1:ii),'Color', 'black','LineWidth', 2.0);
    xlabel('Iteration', 'FontSize', 14, 'FontWeight', 'bold')
    ylabel('Fitness', 'FontSize', 14, 'FontWeight', 'bold')
    drawnow %// you can probably remove this line, as pause already calls drawnow
	thisFrame = getframe(gcf);
    writeVideo(writerObj, thisFrame);
end
close(writerObj);