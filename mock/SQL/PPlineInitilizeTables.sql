CREATE TABLE IF NOT EXISTS "User_" (
  "UserId" SERIAL PRIMARY KEY,
  "Name" text,
  "GroupNameOveride" text,
	"Password" text,
	"About" text,
	"Email" text,
	"Signature" text,
	"Website" text,
	"Description" text,
	"Icon" text

);

CREATE TABLE IF NOT EXISTS "Group_" (
  "GroupId" SERIAL PRIMARY KEY,
  "Name" text,
  "Description" text,
  "Icon" text,
  "User" int,
  FOREIGN KEY ("User") REFERENCES "User_" ("UserId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "Client_" (
  "ClientId" SERIAL PRIMARY KEY,
  "Name" text,
  "Description" text,
  "Icon" text,
  "Group_" int,
  "FilePath" text,
  FOREIGN KEY ("Group_") REFERENCES "Group_" ("GroupId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "Project_" (
  "ProjectId" SERIAL PRIMARY KEY,
  "Name" text,
  "Description" text,
  "Icon" text,
  "ProjectType" text,
  "Client" int,
  "Delivery" blob,
  "Status" int,
  "FilePath" text,
  FOREIGN KEY ("Client") REFERENCES "Client_" ("ClientId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "Scene_" (
  "id" SERIAL PRIMARY KEY,
  "SceneID" text,
  "Version" text,
  "Project" int,
  "Exports" int,
  FOREIGN KEY ("Project") REFERENCES "Project_" ("ProjectId")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "ShotFile_" (
  "id" SERIAL PRIMARY KEY,
  "FilePath" text,
  "SoftwarePackage" timestamp,
  "RenderEngine" int,
  "Shot" int,
  "Exports" int,
  FOREIGN KEY ("Shot") REFERENCES "Shot_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "Shot_" (
  "id" SERIAL PRIMARY KEY,
  "ShotID" text,
  "FullID" text,
  "Version" text,
  "Scene" int,
  "EditFile" int,
  "MainShotFile" int,
  FOREIGN KEY ("Scene") REFERENCES "Scene_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("MainShotFile") REFERENCES "ShotFile_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("EditFile") REFERENCES "EditFileLoadedShots_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "EditFile_" (
  "id" SERIAL PRIMARY KEY,
  "FilePath" text,
  "Version" text,
  "SoftwarePackage" int,
  "Project" int,
  "Exports" int,
  FOREIGN KEY ("Project") REFERENCES "Project_" ("ProjectId")ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("Exports") REFERENCES "Exports_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "EditFileLoadedShots_" (
  "id" SERIAL PRIMARY KEY,
  "EditFile" int
);

CREATE TABLE IF NOT EXISTS "Camera_" (
  "id" SERIAL PRIMARY KEY,
  "CameraName" text,
  "Resolution" text,
  "Version" text,
  "Scene" int,
  "MainShotFile" int,
  "Exports" int
);

CREATE TABLE IF NOT EXISTS "SavedCameraPath_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "Camera" int,
  FOREIGN KEY ("Camera") REFERENCES "Camera_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "CameraKeyframe_" (
  "id" SERIAL PRIMARY KEY,
  "CameraKeyframeList" int,
  "Frame" text,
  "Interpolation" text,
  "PixelAspectRatio" int,
  "Projection" text,
  "FocalLength" int,
  "FilmBack" text,
  "ShutterTime" text,
  "FocusDistance" text,
  "Fstop" text,
  "Bokeh" text,
  "BackgroundImage" text,
  "Transform" int,
  FOREIGN KEY ("Transform") REFERENCES "Transform_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("CameraKeyframeList") REFERENCES "CameraKeyframeList_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "CameraKeyframeList_" (
  "id" SERIAL PRIMARY KEY,
  "Camera" int,
  FOREIGN KEY ("Camera") REFERENCES "Camera_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "Transform_" (
  "id" SERIAL PRIMARY KEY,
  "Position" text,
  "RotationEuler" text,
  "RotationQuaternion" int,
  "Scale" text
);

CREATE TABLE IF NOT EXISTS "TransformKeyframe_" (
  "id" SERIAL PRIMARY KEY,
  "Frame" int,
  "Interpolation" text,
  "Transform" int,
  FOREIGN KEY ("Transform") REFERENCES "Transform_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "RenderEngine_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "RenderEngineName" text,
  "Type" text,
  "CommandArguments" text,
  "Description" text
);

CREATE TABLE IF NOT EXISTS "SoftwarePackage_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "SoftwareName" text,
  "Type" text,
  "CommandArguments" text,
  "Description" text
);

CREATE TABLE IF NOT EXISTS "Exports_" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS "ExportedFile_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "Type" text,
  "Exports" int,
  FOREIGN KEY ("Exports") REFERENCES "Exports_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "PreviewExport_" (
  "id" SERIAL PRIMARY KEY,
  "SoftwarePackage" int,
  "RenderEngine" int,
  "Version" text,
  "Comped" text,
  "CompBatPath" text,
  "FPS" int,
  "Frames" int,
  "StartFrame" int,
  "ShotFile" text,
  "Exports" int,
  FOREIGN KEY ("Exports") REFERENCES "Exports_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("ShotFile") REFERENCES "ShotFile_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("RenderEngine") REFERENCES "RenderEngine_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,
FOREIGN KEY ("SoftwarePackage") REFERENCES "SoftwarePackage_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "FinalExport_" (
  "id" SERIAL PRIMARY KEY,
  "SoftwarePackage" int,
  "RenderEngine" int,
  "Version" text,
  "Comped" text,
  "CompBatPath" text,
  "FPS" int,
  "Frames" int,
  "StartFrame" int,
  "ShotFile" text,
  "Exports" int,
  FOREIGN KEY ("Exports") REFERENCES "Exports_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("ShotFile") REFERENCES "ShotFile_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("RenderEngine") REFERENCES "RenderEngine_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("SoftwarePackage") REFERENCES "SoftwarePackage_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "Delivery_" (
  "id" SERIAL PRIMARY KEY,
  "Version" text,
  "Description" text,
  "DistributionURL" text,
  "DeliveryFiles" int,
  FOREIGN KEY ("DeliveryFiles") REFERENCES "DeliveryFiles_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "DeliveryFiles_" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS "DeliveryFile_" (
  "id" SERIAL PRIMARY KEY,
  "Filepath" text,
  "Type" text,
  "DeliveryFiles" int,
  FOREIGN KEY ("DeliveryFiles") REFERENCES "DeliveryFiles_" ("id")
  ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "PostPipeline" (
  "id" SERIAL PRIMARY KEY,
  "Settings" int,
  "Dependencies" int,
  "Project" int,
  
FOREIGN KEY ("Settings") REFERENCES "PostPipelineSettings" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("Dependencies") REFERENCES "PostPipelineDependencies_" ("id")
ON UPDATE CASCADE
                ON DELETE CASCADE ,

FOREIGN KEY ("Project") REFERENCES "Project_" ("ProjectId")
ON UPDATE CASCADE
                ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS "PostPipelineSettings" (
  "id" SERIAL PRIMARY KEY,
  "ProjectName" text,
  "Version" text,
  "INIPath" text
);

CREATE TABLE IF NOT EXISTS "PostPipelineDependencies_" (
  "id" SERIAL PRIMARY KEY,
  "PipelinePath" text,
  "AudioFile" text,
  "OutputFolder" text,
  "EditJson" text,
  "EditCSV" text
);







