Table User_ {
	UserId int  [pk, increment]
	Name text
	GroupNameOveride text

	Password text

	About text
	Email text
	Signature text
	Website text
	Description text
	Icon text

}





Table Group_ {
	GroupId int [pk, increment]
	Name text
	Description text
	Icon text
	User int

}
Ref: Group_.User > User_.UserId


Table Client_ {
	ClientId int [pk, increment]
	Name text
	Description text
	Icon text
	
	Group_ int
	FilePath text


}
Ref: Client_.Group_ > Group_.GroupId 

Table Project_ {
	ProjectId int [pk, increment]
	Name text
	Description text
	Icon text
	ProjectType text
	Client int
	Delivery blob
	Status int
	FilePath text

}

Ref: Project_.Client >  Client_.ClientId 


Ref: ShotFile_.Shot >  Shot_.id 

// Creating tables
Table Scene_ as U {
  id int [pk, increment] // auto-increment
  SceneID text
  Version text
  Project int
  Exports int
}

Ref: Scene_.Project >  Project_.ProjectId 



// Creating Shots
Table ShotFile_ as U {
  id int [pk, increment] // auto-increment
  FilePath text
  SoftwarePackage timestamp
  RenderEngine int
  Shot int
  Exports int
}



Table Shot_ as U {
  id int [pk, increment] // auto-increment
  ShotID text
  FullID text
  Version text
  Scene int
  EditFile int
  MainShotFile int
}

Ref: Shot_.Scene >  Scene_.id 
Ref: Shot_.MainShotFile >  ShotFile_.id 
Ref: Shot_.EditFile >  EditFileLoadedShots_.id 


// Edit Files


Table EditFile_ as U {
  id int [pk, increment] // auto-increment
  FilePath text
  Version text
  SoftwarePackage int
  Project int
  Exports int
}
Ref: EditFile_.Project >  Project_.ProjectId 
Ref: EditFile_.Exports >  Exports_.id 

Table EditFileLoadedShots_ as U {
  id int [pk, increment] // auto-increment
  EditFile int
}




// Camera
Table Camera_ as U {
  id int [pk, increment] // auto-increment
  CameraName text
  Resolution text
  Version text
  Scene int
  MainShotFile int
  Exports int
}
Table SavedCameraPath_ as U {
  id int [pk, increment] // auto-increment
  Filepath text
  Camera int
}

Ref: SavedCameraPath_.Camera >  Camera_.id 

Table CameraKeyframe_ as U {
  id int [pk, increment] // auto-increment
  CameraKeyframeList int
  Frame text
  Interpolation text
  PixelAspectRatio int
  Projection text
  FocalLength int
  FilmBack text
  ShutterTime text
  FocusDistance text
  Fstop text
  Bokeh text
  BackgroundImage text

  Transform int
}
Ref: CameraKeyframe_.Transform >  Transform_.id 


Ref: CameraKeyframe_.CameraKeyframeList >  CameraKeyframeList_.id 

Table CameraKeyframeList_ as U {
  id int [pk, increment] // auto-increment
  Camera int
}
Ref: CameraKeyframeList_.Camera >  Camera_.id 



// Transforms
Table Transform_ as U {
  id int [pk, increment] // auto-increment
  Position text
  RotationEuler text
  RotationQuaternion int
  Scale text
}

Table TransformKeyframe_ as U {
  id int [pk, increment] // auto-increment
  Frame int
  Interpolation text
  Transform int
}
Ref: TransformKeyframe_.Transform >  Transform_.id 

Table RenderEngine_ as U {
  id int [pk, increment] // auto-increment
  Filepath text
  RenderEngineName text
  Type text
  CommandArguments text
  Description text
}


Table SoftwarePackage_ as U {
  id int [pk, increment] // auto-increment
  Filepath text
  SoftwareName text
  Type text
  CommandArguments text
  Description text
  //RenderEngine int
}
// Ref: SoftwarePackage_.RenderEngine >  RenderEngine_.id 



// Exports

Table Exports_ as U {
  id int [pk, increment] // auto-increment

}



Table ExportedFile_ as U {
  id int [pk, increment] // auto-increment
  Filepath text
  Type text
  Exports int
}
Ref: ExportedFile_.Exports >  Exports_.id 


Table PreviewExport_ as U {
  id int [pk, increment] // auto-increment
  SoftwarePackage int
  RenderEngine int
  Version text
  Comped text
  CompBatPath text
  FPS int
  Frames int
  StartFrame int
  ShotFile text
  Exports int
}
Ref: PreviewExport_.Exports >  Exports_.id 
Ref: PreviewExport_.ShotFile >  ShotFile_.id 
Ref: PreviewExport_.RenderEngine >  RenderEngine_.id 
Ref: PreviewExport_.SoftwarePackage >  SoftwarePackage_.id 


Table FinalExport_ as U {
  id int [pk, increment] // auto-increment
  SoftwarePackage int

  RenderEngine int
  Version text
  Comped text
  CompBatPath text
  FPS int
  Frames int
  StartFrame int
  ShotFile text
  Exports int
}
Ref: FinalExport_.Exports >  Exports_.id 
Ref: FinalExport_.ShotFile >  ShotFile_.id 
Ref: FinalExport_.RenderEngine >  RenderEngine_.id 
Ref: FinalExport_.SoftwarePackage >  SoftwarePackage_.id 


// Delivery
Table Delivery_ as U {
  id int [pk, increment] // auto-increment
  Version text
  Description text
  DistributionURL text
  DeliveryFiles int
}
Ref: Delivery_.DeliveryFiles >  DeliveryFiles_.id 


Table DeliveryFiles_ as U {
  id int [pk, increment] // auto-increment
}

Table DeliveryFile_ as U {
  id int [pk, increment] // auto-increment
  Filepath text
  Type text
  DeliveryFiles int
}

Ref: DeliveryFile_.DeliveryFiles >  DeliveryFiles_.id 






Table PostPipeline as U {
  id int [pk, increment] // auto-increment
  Settings int
  Dependencies int
  Project int

}
Ref: PostPipeline.Settings >  PostPipelineSettings.id 
Ref: PostPipeline.Dependencies >  PostPipelineDependencies_.id 
Ref: PostPipeline.Project >  Project_.ProjectId 


Table PostPipelineSettings as U {
  id int [pk, increment] // auto-increment
  ProjectName text
  Version text
  INIPath text

}


Table PostPipelineDependencies_ as U {
  id int [pk, increment] // auto-increment
  PipelinePath text
  AudioFile text
  OutputFolder text
  EditJson text
  EditCSV text
}
