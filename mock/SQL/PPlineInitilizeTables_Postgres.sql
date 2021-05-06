CREATE TABLE IF NOT EXISTS public."User_" (
  "UserId" SERIAL PRIMARY KEY,
  "Name" character varying(500),
  "GroupNameOveride" character varying(500),
	"Password" character varying(500),
	"About" character varying(500),
	"Email" character varying(500),
	"Signature" character varying(500),
	"Website" character varying(500),
	"Description" character varying(500),
	"Icon" character varying(500)

);

CREATE TABLE IF NOT EXISTS public."Group_" (
  "GroupId" SERIAL PRIMARY KEY,
  "Name" character varying(500),
  "Description" character varying(500),
  "Icon" character varying(500),
  "User" int,
  FOREIGN KEY ("User") REFERENCES public."User_" ("UserId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."Client_" (
  "ClientId" SERIAL PRIMARY KEY,
  "Name" character varying(500),
  "Description" character varying(500),
  "Icon" character varying(500),
  "Group_" int,
  "FilePath" character varying(500),
  FOREIGN KEY ("Group_") REFERENCES public."Group_" ("GroupId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."Project_" (
  "ProjectId" SERIAL PRIMARY KEY,
  "Name" character varying(500),
  "Description" character varying(500),
  "Icon" character varying(500),
  "ProjectType" character varying(500),
  "Client" int,
  "Delivery" int,
  "Status" int,
  "FilePath" character varying(500),
  FOREIGN KEY ("Client") REFERENCES public."Client_" ("ClientId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."Scene_" (
  id SERIAL,
PRIMARY KEY (id),
  "SceneID" character varying(500),
  "Version" character varying(500),
  "Project" int,
  "Exports" int,
  FOREIGN KEY ("Project") REFERENCES public."Project_" ("ProjectId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."ShotFile_" (
  id SERIAL,
PRIMARY KEY (id),
  "FilePath" character varying(500),
  "SoftwarePackage" int,
  "RenderEngine" int,
  "Shot" int,
  "Exports" int

);

CREATE TABLE IF NOT EXISTS public."Shot_" (
  id SERIAL,
PRIMARY KEY (id),
  "ShotID" character varying(500),
  "FullID" character varying(500),
  "Version" character varying(500),
  "Scene" int,
  "EditFile" int,
  "MainShotFile" int,
  FOREIGN KEY ("Scene") REFERENCES public."Scene_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("MainShotFile") REFERENCES public."ShotFile_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 


);

ALTER TABLE public."ShotFile_"
    ADD CONSTRAINT fk_shot_shotfile FOREIGN KEY ("Shot") REFERENCES public."Shot_" ("id");

CREATE TABLE IF NOT EXISTS public."EditFile_" (
  id SERIAL,
PRIMARY KEY (id),
  "FilePath" character varying(500),
  "Version" character varying(500),
  "SoftwarePackage" int,
  "Project" int,
  "Exports" int,
  FOREIGN KEY ("Project") REFERENCES public."Project_" ("ProjectId")ON UPDATE CASCADE
                ON DELETE CASCADE 



);

CREATE TABLE IF NOT EXISTS public."EditFileLoadedShots_" (
  id SERIAL,
PRIMARY KEY (id),
  "EditFile" int
);

ALTER TABLE public."Shot_"
    ADD CONSTRAINT fk_ShotFile__EditFile FOREIGN KEY ("EditFile") REFERENCES public."EditFileLoadedShots_" ("id");

CREATE TABLE IF NOT EXISTS public."Camera_" (
  id SERIAL,
PRIMARY KEY (id),
  "CameraName" character varying(500),
  "Resolution" character varying(500),
  "Version" character varying(500),
  "Scene" int,
  "MainShotFile" int,
  "Exports" int
);

CREATE TABLE IF NOT EXISTS public."SavedCameraPath_" (
  id SERIAL,
PRIMARY KEY (id),
  "Filepath" character varying(500),
  "Camera" int,
  FOREIGN KEY ("Camera") REFERENCES public."Camera_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."CameraKeyframe_" (
  id SERIAL,
PRIMARY KEY (id),
  "CameraKeyframeList" int,
  "Frame" character varying(500),
  "Interpolation" character varying(500),
  "PixelAspectRatio" int,
  "Projection" character varying(500),
  "FocalLength" int,
  "FilmBack" character varying(500),
  "ShutterTime" character varying(500),
  "FocusDistance" character varying(500),
  "Fstop" character varying(500),
  "Bokeh" character varying(500),
  "BackgroundImage" character varying(500),
  "Transform" int
  

);

CREATE TABLE IF NOT EXISTS public."CameraKeyframeList_" (
  id SERIAL,
PRIMARY KEY (id),
  "Camera" int,
  FOREIGN KEY ("Camera") REFERENCES public."Camera_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."Transform_" (
  id SERIAL,
PRIMARY KEY (id),
  "Position" character varying(500),
  "RotationEuler" character varying(500),
  "RotationQuaternion" int,
  "Scale" text
);
  ALTER TABLE public."CameraKeyframe_"
    ADD CONSTRAINT fk_CameraKeyframe_Transform FOREIGN KEY ("Transform") REFERENCES public."Transform_" ("id");

  ALTER TABLE public."CameraKeyframe_"
    ADD CONSTRAINT fk_CameraKeyframe_CameraKeyframeList FOREIGN KEY ("CameraKeyframeList") REFERENCES public."CameraKeyframeList_" ("id");

CREATE TABLE IF NOT EXISTS public."TransformKeyframe_" (
  id SERIAL,
PRIMARY KEY (id),
  "Frame" int,
  "Interpolation" character varying(500),
  "Transform" int,
  FOREIGN KEY ("Transform") REFERENCES public."Transform_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."RenderEngine_" (
  id SERIAL,
PRIMARY KEY (id),
  "Filepath" character varying(500),
  "RenderEngineName" character varying(500),
  "Type" character varying(500),
  "CommandArguments" character varying(500),
  "Description" text
);

CREATE TABLE IF NOT EXISTS public."SoftwarePackage_" (
  id SERIAL,
PRIMARY KEY (id),
  "Filepath" character varying(500),
  "SoftwareName" character varying(500),
  "Type" character varying(500),
  "CommandArguments" character varying(500),
  "Description" text
);

CREATE TABLE IF NOT EXISTS public."Exports_" (
  "id" SERIAL PRIMARY KEY
);
ALTER TABLE public."EditFile_"
    ADD CONSTRAINT fk_shot_export FOREIGN KEY ("Exports") REFERENCES public."Exports_" ("id");

CREATE TABLE IF NOT EXISTS public."ExportedFile_" (
  id SERIAL,
PRIMARY KEY (id),
  "Filepath" character varying(500),
  "Type" character varying(500),
  "Exports" int,
  FOREIGN KEY ("Exports") REFERENCES public."Exports_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."PreviewExport_" (
  id SERIAL,
PRIMARY KEY (id),
  "SoftwarePackage" int,
  "RenderEngine" int,
  "Version" character varying(500),
  "Comped" character varying(500),
  "CompBatPath" character varying(500),
  "FPS" int,
  "Frames" int,
  "StartFrame" int,
  "ShotFile" int,
  "Exports" int,
  FOREIGN KEY ("Exports") REFERENCES public."Exports_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("ShotFile") REFERENCES public."ShotFile_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("RenderEngine") REFERENCES public."RenderEngine_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,
FOREIGN KEY ("SoftwarePackage") REFERENCES public."SoftwarePackage_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."FinalExport_" (
  id SERIAL,
PRIMARY KEY (id),
  "SoftwarePackage" int,
  "RenderEngine" int,
  "Version" character varying(500),
  "Comped" character varying(500),
  "CompBatPath" character varying(500),
  "FPS" int,
  "Frames" int,
  "StartFrame" int,
  "ShotFile" int,
  "Exports" int,
  FOREIGN KEY ("Exports") REFERENCES public."Exports_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("ShotFile") REFERENCES public."ShotFile_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("RenderEngine") REFERENCES public."RenderEngine_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("SoftwarePackage") REFERENCES public."SoftwarePackage_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."Delivery_" (
  id SERIAL,
PRIMARY KEY (id),
  "Version" character varying(500),
  "Description" character varying(500),
  "DistributionURL" character varying(500),
  "DeliveryFiles" int
);

CREATE TABLE IF NOT EXISTS public."DeliveryFiles_" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS public."DeliveryFile_" (
  id SERIAL,
PRIMARY KEY (id),
  "Filepath" character varying(500),
  "Type" character varying(500),
  "DeliveryFiles" int,
  FOREIGN KEY ("DeliveryFiles") REFERENCES public."DeliveryFiles_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);
ALTER TABLE public."Delivery_"
    ADD CONSTRAINT fk_Delivery_DeliveryFiles  FOREIGN KEY ("DeliveryFiles") REFERENCES public."DeliveryFiles_" ("id");

CREATE TABLE IF NOT EXISTS public."PostPipeline" (
  id SERIAL,
PRIMARY KEY (id),
  "Settings" int,
  "Dependencies" int,
  "Project" int,


FOREIGN KEY ("Project") REFERENCES public."Project_" ("ProjectId")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS public."PostPipelineSettings" (
  id SERIAL,
PRIMARY KEY (id),
  "ProjectName" character varying(500),
  "Version" character varying(500),
  "INIPath" text
);

CREATE TABLE IF NOT EXISTS public."PostPipelineDependencies_" (
  id SERIAL,
PRIMARY KEY (id),
  "PipelinePath" character varying(500),
  "AudioFile" character varying(500),
  "OutputFolder" character varying(500),
  "EditJson" character varying(500),
  "EditCSV" text
);




ALTER TABLE public."PostPipeline"
    ADD CONSTRAINT fk_PostPipeline_Settings FOREIGN KEY ("Settings") REFERENCES public."PostPipelineSettings" ("id");

ALTER TABLE public."PostPipeline"
ADD CONSTRAINT fk_PostPipeline_Dependencies FOREIGN KEY ("Dependencies") REFERENCES public."PostPipelineDependencies_" ("id");


