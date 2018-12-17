%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                                     %
%                               Detect People in an Image                             %
%                              KDI Project - a.y 2018/2019                            %
%                      Giorgia Gobbi, Cristiano Saltori, Alex Bojeri                  %
%                                                                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Create detector objects 

   %Face detector
    faceDetector = vision.CascadeObjectDetector; 
   %Upper body detector
    bodyDetector = vision.CascadeObjectDetector('UpperBody'); 
    bodyDetector.MinSize = [60 60];
    bodyDetector.MergeThreshold = 10;
   %People detector
    peopleDetector = peopleDetectorACF;
       

%% Choose folder path
    if ~exist('PATH', 'var') || ~ischar(PATH) || ~exist(PATH, 'dir')
        PATH = uigetdir('.', 'Choose the folder');
    end

%% Read input images

    folder = dir(fullfile(PATH,'*.jpg'));
    last_image_index = numel(folder);
    image_index_array = 1:last_image_index;

     %Save Folder path
             I=imfinfo(image_path);
             FileName='sd1_db.csv';
             file=fopen(fullfile(pwd,FileName),'w');
             fprintf(file, 'FileName, FileDate, Format \n');
        
    
    for image_index = image_index_array

        fprintf('Image #%d - Processing started. \n', image_index)
        image_path = fullfile(PATH,folder(image_index).name);
        image = imread(image_path);
        image_name=folder(image_index).name;
        %% Detect faces, upper body and people
        bboxesFace = step(faceDetector, image); %Detect faces with Viola-Jones Algorithm
        bboxesBody = step(bodyDetector, image); %Detect upper body with Viola-Jones Algorithm
        [bboxesPeople,scoreP] = detect(peopleDetector,image); %Detect people using aggregate channel features
        
          
        %% Check the results:
        %  If faces/upper body/people are not detected from each detector save as _NoPeople, else save as _People                     
        if((isempty(bboxesFace))&&(isempty(bboxesBody))&&(isempty(bboxesPeople)))
            people=false;
            disp('no people');
                   
            [sourceFolder, baseFileNameNoExtenstion, ext] = fileparts(image_path);
            outputBaseName = [baseFileNameNoExtenstion, '_noPeople.jpg'];
            fullDestinationFileName = fullfile(PATH, outputBaseName);
            imwrite(image, fullDestinationFileName);

        else 
            people=true;
            disp('people');

            % Write imgs with people indication
            [sourceFolder, baseFileNameNoExtenstion, ext] = fileparts(image_path);
            outputBaseName = [baseFileNameNoExtenstion, '_People.jpg'];
            fullDestinationFileName = fullfile(PATH, outputBaseName);
            imwrite(image, fullDestinationFileName);
        end
    end



    
    
   
   
   